Title: java 策略模式  
Slug: java ,  策略  
Date: 2014-01-13 15:21:38  
Tags: java , 设计模式  
Category: 设计模式  
Author: 泽  
Lang: zh  
Summary: java 策略模式  



java 策略模式
===============================
- 动态的改变对象的行为  
- 可以组合调整类的表现方式  

:::java
       

    package com.weidou.mota.patterns.policy;

    public class PoLicyDemo {

        //吃相接口
        public interface Eat {
            public String eat(); //返回吃相接口
        }

        //外表接口
        public interface Surface {
            public String surface();//返回外表字符串
        }

        /**
         * 
         * StrongEat 吃相不雅
         * 
         * @author lixuze
         *
         */
        public static class StrongEat implements Eat {
            @Override
            public String eat() {
                return "狼吞虎咽";
            }
        }

        public static class QuietEat implements Eat {
            @Override
            public String eat() {
                return "慢嚼细咽";
            }
        }

        public static class BeautySurface implements Surface {
            @Override
            public String surface() {
                return "杨柳细腰";
            }
        }

    
        public static class StrongSurface implements Surface {
            @Override
            public String surface() {
                return "抠脚大汉";
            }
        }

        /**
         * 
         * 实现人的祖类
         * @author lixuze
         *
         */
        public static class People {
            private Eat eat = null;
            private Surface surface = null;

            public People(Eat eat, Surface surface) {
                this.eat = eat;
                this.surface = surface;
            }

            /**
             * 输出 吃相及外观
             */
            public void doAction() {
                System.out.println("吃饭的样子 : " + this.eat.eat() + "\t 外表 : " +this.surface.surface());
            }
        }

        //男人类
        public static class Man extends People {
            public Man() {
                super(new StrongEat(), new StrongSurface());
            }
        }

        //女人类
        public static class Woman extends People {
            public Woman() {
                super(new QuietEat(), new BeautySurface());
            }
        }

        //女汉子类
        public static class ToughGirl extends People {
            public ToughGirl() {
                super(new StrongEat(), new BeautySurface());
            }
        }
        public static void main(String[] args) {
            new Man().doAction();
            new Woman().doAction();
            new ToughGirl().doAction();
        }
      }

总结
-----------------
为什么用这个模式 ， 我们如果想表现更多的“类型”人，组合添加就可以， 将表现的方法 ， 与类的逻辑分开 ，可以使得模块独立 ， 更加具有灵活性
