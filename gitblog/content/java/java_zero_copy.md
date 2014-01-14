Title: java 零拷贝(zero copy)  
Slug: java 零拷贝  
Date: 2014-01-07 00:26:35  
Tags: java , 技术  
Category: 技术  
Author: 泽  
Lang: zhs  
Summary: java zero copy



java 零拷贝技术(zero copy) 大文件拷贝
---------------------------------------
- 为完成公司的拷贝任务（很多文件分布在很多文件夹 ，必须整理固定大小文件，存储在一个文件夹中）  
- 文件特别大，过去的io工具，多线程，慢（我的理解是读取文件时，磁盘是指针寻址，增加磁盘读取时间）  
- 零拷贝（我理解为，磁盘存取是块来存取的，我们读取文件的时候，整块读，速度肯定很快）  


:::java
       
       package com.weidou.mota.output;		

		import java.io.File;
		import java.io.FileInputStream;
		import java.io.FileNotFoundException;
		import java.io.FileOutputStream;
		import java.io.IOException;
		import java.nio.channels.FileChannel;
		import java.util.ArrayList;
		import java.util.HashSet;
		import java.util.List;
		import java.util.Set;
		import java.util.concurrent.BlockingQueue;
		import java.util.concurrent.LinkedBlockingDeque;

		public class FileSuper {
	
		public static final long KB = 1024l;
		public static final long MB = 1024 * KB;
		public static final long GB = 1024 * MB;

		private FileSuper() {	

		}

	public static Set<File> folderWalk(String path) {
		File folder = new File(path);
		Set<File> fileList = new HashSet<File>();
		for (File file : folder.listFiles()) {
			if (file.isDirectory()) {
				fileList.addAll(folderWalk(file.getAbsolutePath()));
			} else {
				fileList.add(file);
			}
		}
		return fileList;
	}

	public static boolean spiltFilesBySize(BlockingQueue<File> fileQueue,
			final long dataSize, File outPutDir, final String fileSuffix,
			final String filePrex) throws IOException {
		if (!(outPutDir.isDirectory() && outPutDir.exists())) {
			throw new IllegalArgumentException("不存在路径 或者路径不是文件夹 :"
					+ outPutDir.getAbsolutePath());
		}
		long remainSize = 0;// 要生成的文件还有剩余大小
		int outFileSeq = 1; //输出文件序号
		long fileInSize = 0; //输入文件大小
		long fileInRemainSize = 0; //文件剩下的大小
		FileChannel outFile = null; //文件输出nio
		FileChannel fileIn = null; //文件输入nio
		while (!fileQueue.isEmpty()) { //看是否还有文件
			if (fileInRemainSize <= 0) {//如果输入文件已经全部存入
				if (fileIn != null) { //判断文件是否为空
					fileIn.close(); //关闭输入文件
					fileIn = null; //输入文件为null
				}
				File filePoll = fileQueue.poll(); //取得一个输入文件
				fileIn = getInfile(filePoll); //获得读入文件nio
				fileInRemainSize = fileIn.size(); // 文件的指针 = fileInSize -
													// fileInRemainSize
				fileInSize = fileIn.size(); //记录文件大小
			}
			if (remainSize <= 0) { //距离一个生成的文件还有多少
				if (outFile != null) { //输出文件不为空
					outFile.close(); //输入文件关闭
				}
				outFile = getOutFile(outPutDir, fileSuffix, filePrex,
						outFileSeq); //生成一个文件输出nio
				outFileSeq = outFileSeq + 1; //序列号 + 1
				remainSize = dataSize; //重置文件输出大小
			}

			long cutFileInPoint = 0l; //文件结构 [已经输出大小 + fileInRemainSize ] <=fileInSize
			if (fileInRemainSize > remainSize) { 
				cutFileInPoint = remainSize;
				remainSize = 0;
			} else if (fileInRemainSize <= remainSize) {
				cutFileInPoint = fileInRemainSize;
				remainSize = remainSize - cutFileInPoint;
			}
			//这块是重点 nio 不支持大于4g数据的复制，所以一块块复制(切片复制)
			for (long count = 0; count <= cutFileInPoint; count = count
					+ 70 * MB) { //这里粗犷的处理 , 因为文件数据很多丢失 《 70 mb 不算什么
				fileIn.transferTo(fileInSize - fileInRemainSize + count,
						70 * MB, outFile); //复制
			}
			fileInRemainSize = fileInRemainSize - cutFileInPoint; //
		}
		return true;
	}

	@SuppressWarnings("resource")
	public static FileChannel getInfile(File file) throws FileNotFoundException {
		return new FileInputStream(file).getChannel();
	}

	@SuppressWarnings("resource")
	public static FileChannel getOutFile(File outPutDir,
			final String fileSuffix, final String filePrex, int outFileSeq)
			throws FileNotFoundException {
		return new FileOutputStream(new File(outPutDir.getAbsolutePath() + "/"
				+ fileSuffix + outFileSeq + filePrex)).getChannel();
	}

	
	
	
	public static void main(String args []) throws IOException
	{
		if (args.length < 4) {
			throw new IllegalArgumentException("参数太少");
		}
		List<String> inputPaths = new ArrayList<String>();
		String prex = "NO_";
		String suffix = ".csv";
		long size = FileSplit.GB * 50;
		File output = null;

			for (int i = 0; i < args.length; i++) {
				String choice = args[i];
				if (choice.equals("--filelist")) {
					for (String path : args[i + 1].split("#")) {
						inputPaths.add(path.trim());
					}
					i = i + 1;
				} else if (choice.equals("--prex")) {
					prex = args[i + 1];
					i = i + 1;
				} else if (choice.equals("--suffix")) {
					suffix = args[i + 1];
					i = i + 1;
				} else if (choice.equals("--output")) {
					output = new File(args[i + 1]);
					i = i + 1;
				} else if (choice.equals("--filegb")) {	

				}
			}
			if (StringUtils.isEmpty(prex) || StringUtils.isEmpty(suffix)
					|| inputPaths.size() <= 0 || output == null) {
				throw new IllegalArgumentException("输入参数有误!");
			}
			BlockingQueue<File> fileQueue = new LinkedBlockingDeque<File>();
			for (String path : inputPaths) {
				fileQueue.addAll(folderWalk(path));
			}
			spiltFilesBySize(fileQueue, size, output, prex, suffix);
		}
	}


总结
----------------------------
我写这个是在看数据生成，拭了很多把都失败了，刚开始心急如焚，后来继续测试，用了过去读取文件（按行），在写（慢死）  
不过最后写出来了 ， 里面虽然少了很多对异常的判断 ，但是基本可以满足使用  
已经夜里1点了 看来我在等到很晚才睡 ，各位晚安  
