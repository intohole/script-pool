Title: java 工厂模式  
Slug: java pattern  
Date: 2014-01-03 10:35:20  
Tags: java,设计模式,工厂  
Category: java
Author: 泽  
Lang: zh  
Summary: java 设计模式  




java 工厂模式  
=======================================

java:::
       

       /**
        * 定义一个关于吃相和外观的方法
        * 
        * 
        * @author lixuze
        *
       */
       public interface IEatSurface {
              public void eat();//吃相
              public void surface();//外观 
        }


        /**
         * 男人类
         * 
         * 吃相粗野
         * 外表很强悍
         * 
         * @author lixuze
         *
         */
        public class ManEat implements IEatSurface{
            @Override
            public void eat() {
                System.out.println("狼吞虎咽的吃");
                
            }
            @Override
            public void surface() {
                System.out.println("虎背熊腰");
            }
        }



        /**
        * 女汉子
         * 吃相男人 外表女人
         * 
         * @author lixuze
         *
         */
        public class ToughGirl implements IEatSurface{

            @Override
            public void eat() {
                System.out.println("狼吞虎咽的吃");
            }

            @Override
            public void surface() {
                System.out.println("楊柳細腰");
            }

        }


        /**
         * 女人
         * 吃相斯文
         * 外表柔弱
         * 
         * 
         * @author lixuze
         *
         */
        public class WomanEat implements IEatSurface{

            @Override
            public void eat() {
                System.out.println("细嚼慢咽的吃");
                    
            }

            @Override
            public void surface() {
                System.out.println("楊柳細腰");
                       
            }
        }


        import java.util.ArrayList;
        import java.util.List;

        import com.weidou.mota.patterns.factory.EatSurfaceFactory.PEOPLE_TYPE;

        class People {
            private String name;
            private PEOPLE_TYPE type;

            public People(String name, PEOPLE_TYPE type) {
                this.name = name;
                this.type = type;
            }

            public String getName() {
                return name;
            }

            public void setName(String name) {
                this.name = name;
            }

            public PEOPLE_TYPE getType() {
                return type;
            }

            public void setType(PEOPLE_TYPE type) {
                this.type = type;
            }
        }

        public class EatSurfaceFactory {        

            public enum PEOPLE_TYPE {
                MAN("男人"), WOMAN("女人"), TOUGHGIRL("女汉子");
                private String value;       

                private PEOPLE_TYPE(String name) {
                    this.value = name;
                }       

                public String getValue() {
                    return this.value;
                }
        }
        /**
         * 生成一个吃相外观类
         * @param name 类型
         * @return 吃相外观类
         * @throws NoSuchMethodException 如果name 不存在方法类中，没有实现的功能方法
         */
        public static IEatSurface getEatSurface(String name)
                throws NoSuchMethodException {
            if (name == null || name.equals("")) {
                throw new IllegalArgumentException("名称不能为空");
            }
            if (name.trim().equals("男人")) {
                return new ManEat();
            } else if (name.trim().equals("女人")) {
                return new WomanEat();
            } else if (name.trim().equals("女汉子")) {
                return new ToughGirl();
            } else {
                throw new NoSuchMethodException("没有实现 :" + name + "\t 方法");
            }
        }

        public static IEatSurface getEatSurface(PEOPLE_TYPE type)
                throws NoSuchMethodException {
            return getEatSurface(type.getValue());
        }

        public static void main(String args[]) {
            List<People> peoples = new ArrayList<People>();
            peoples.add(new People("王妹", PEOPLE_TYPE.WOMAN));
            peoples.add(new People("张三", PEOPLE_TYPE.MAN));
            peoples.add(new People("龚爱丽", PEOPLE_TYPE.TOUGHGIRL));
            for (People people : peoples) {
                IEatSurface es = null;
                try {
                    es = getEatSurface(people.getType());
                } catch (NoSuchMethodException e) {
                    System.out.println(e);
                    continue;
                }
                System.out.println(people.getName() + "\t 吃相:" + es.eat() + "\t外观:" + es.surface());
            }
        }   

    }



总结:
-------------------------
为系统结构提供灵活的动态扩展机制.减速少工作量,方便维护,是一种把功能解除耦合 ,比如 商品店打折  

赘述
--------------------------
关于上面代码在探讨，发现原来吃只有几种 , 外貌有几种，但是如果更为多的组合方式哪，类似女汉子类的实现方式就有待改进，我们可以把吃相在进一步颗粒话，生成一个关于吃相的工厂模式,外貌也如此 ， 这样我们就会可以组合更多的功能。  
* 代码尽可量有注释  
* 函数功能更加具体,颗粒话  

