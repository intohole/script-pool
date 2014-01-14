Title: java 观察者  
Slug: java obsever  
Date: 2013-12-29 12:42:41  
Tags: java,设计模式  
Category: 设计模式  
Author: 泽仔  
Lang: zh  
Summary:  java 观察者设计模式  


java 观察者  
=======================



:::java  
       
       	import java.util.LinkedHashMap;
		import java.util.Map;

		import org.apache.log4j.Logger;




		/**
		*注册者 
		*
		*
		*
		*/
		public abstract class ControlerMethod<T, E,U> {

				private static final Logger logger = Logger.getLogger(ControlerMethod.class);
				// 存储搜索接口的map
				protected Map<String, T> methoMap = new LinkedHashMap<String, T>();

				/**
				 * 添加使用的接口
				 * 
				 * @param bookSearch
				 *            搜索接口
				 * @return true 添加 false 接口为空 或者 已经存在这个接口
				 */
				public synchronized boolean registerMethod(T method) {
					if (method == null
							|| methoMap.containsKey(method.getClass().getName())) {
						logger.info("方法为空 ， 或者已经存在方法 : " + method);
						return false;
					}
					logger.info("添加注册方法 : " + method.getClass().getName());
					this.methoMap.put(method.getClass().getName(), method);
					return true;
				}

				/**
				 * 移除要使用的接口
				 * 
				 * @param bookSearch
				 *            搜索接口
				 * @return
				 */
				public synchronized boolean removeMethod(T method) {
					if (method == null || !methoMap.containsKey(method.getClass().getName())) {
						return false;
					}
					logger.info("移除接口 : " + method.getClass().getName());
					this.methoMap.remove(method.getClass().getName());
					return true;
				}

				public abstract E getMethodResult(U seed);
		}
