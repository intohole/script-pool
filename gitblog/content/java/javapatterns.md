Date: 2013-12-12 08:59:31
Title: Java  Builder  
slug: java  
Tags: Java  
Category: 设计模式  

JAVA BUILDER
---------------------------


:::java

    public class TimeStringBuffer {
        private StringBuffer timeBuffer = new StringBuffer();
        public TimeStringBuffer setHH() {
            timeBuffer.append("hh"); 
            return this; // 设置时返回自己指针 -》 方便后续方法调用自己的方法
        }
        public TimeStringBuffer setMM() {
            timeBuffer.append("mm"); 
            return this;
        }
        public String make() { //参数最后输出方法 关键
            return this.timeBuffer.toString();
        }
        public static void main(String[] args) {
            TimeStringBuffer buffer = new TimeStringBuffer(); buffer.setHH().setMM();
            System.out.println(buffer.make());
        }
    }
