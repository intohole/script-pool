Date: 2013-12-11 19:55:20  
Title: Java 设计模式  
slug: java    
Tags: java  
Category: 学习   



JAVA BUILDER
-------------

:::java
    public class TimeStringBuffer {

        private StringBuffer timeBuffer = new StringBuffer();
w
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