
## Java简介
### 基础
#### Java介于编译型语言和解释型语言之间。
- 编译型语言如C、C++，代码是直接编译成机器码执行，但是不同的平台（x86、ARM等）CPU的指令集不同，因此，需要编译出每一种平台的对应机器码。        
- 解释型语言如Python、Ruby没有这个问题，可以由解释器直接加载源码然后运行，代价是运行效率太低。
- 而Java是将代码编译成一种“字节码”，它类似于抽象的CPU指令，然后，针对不同平台编写虚拟机，不同平台的虚拟机负责加载字节码并执行，这样就实现了“一次编写，到处运行”的效果。
- 当然，这是针对Java开发者而言。对于虚拟机，需要为每个平台分别开发。为了保证不同平台、不同公司开发的虚拟机都能正确执行Java字节码，SUN公司制定了一系列的Java虚拟机规范。从实践的角度看，JVM的兼容性做得非常好，低版本的Java字节码完全可以正常运行在高版本的JVM上.
#### JDK和JRE
- JDK：Java Development Kit
- JRE：Java Runtime Environment
- 简单地说，JRE就是运行Java字节码的虚拟机。但是，如果只有Java源码，要编译成Java字节码，就需要JDK，因为JDK除了包含JRE，还提供了编译器、调试器等开发工具.
#### 如何运行Java程序
- 一个Java源码只能定义一个public类型的class，并且class名称和文件名要完全一致；
- Java源码本质上是一个文本文件，我们需要先用javac把Hello.java编译成字节码文件Hello.class，然后，用java命令执行这个字节码文件;
- 使用javac可以将.java源码编译成.class字节码；使用java可以运行一个已编译的Java程序，参数是类名.

#### Java程序基本结构
- 类名必须以英文字母开头，后接字母，数字和下划线的组合习惯以大写字母开头
- 对于float类型，需要加上f后缀
- 定义变量的时候，如果加上final修饰符，这个变量就变成了常量，常量的作用是用有意义的变量名来避免魔术数字（Magic number）
- Java提供了两种变量类型：基本类型和引用类型；基本类型包括整型，浮点型，布尔型，字符型。变量可重新赋值，等号是赋值语句，不是数学意义的等号。常量在初始化后不可重新赋值，使用常量便于理解程序意图.
#### 整数运算
- 整数运算的结果永远是精确的；
- 运算结果会自动提升；
- 可以强制转型，但超出范围的强制转型会得到错误的结果；
- 应该选择合适范围的整型（int或long），没有必要为了节省内存而使用byte和short进行整数运算.

#### 布尔运算
- 避免短路运算boolean isPrimaryStudent = age >=6?(age <= 12?true:false):false;
#### 字符和字符串
-  Java的字符类型char是基本类型，字符串类型String是引用类型；
- 基本类型的变量是“持有”某个数值，引用类型的变量是“指向”某个对象；
- 引用类型的变量可以是空值null；要区分空值null和空字符串"".
#### 数组
- 数组是同一数据类型的集合，数组一旦创建后，大小就不可变；
- 可以通过索引访问数组元素，但索引超出范围将报错；
- 数组元素可以是值类型（如int）或引用类型（如String），但数组本身是引用类型.
#### 输入输出
- println是print line的缩写，表示输出并换行。因此，如果输出后不想换行，可以用print()；
- 占位符   

|  占位符   | 说明  |
|  :----:  |:----:  |
| %d  | 格式化输出整数 |
| %x  | 格式化输出十六进制整数 |
| %f  | 格式化输出浮点数  |
| %e  | 格式化输出科学计数法表示的浮点数 |
| %s  | 格式化字符串 |
- Java提供的输出包括：System.out.println() / print() / printf()，其中printf()可以格式化输出；
- Java提供Scanner对象来方便输入，读取对应的类型可以使用：scanner.nextLine() / nextInt() / nextDouble() / ...
#### if判断
- if ... else可以做条件判断，else是可选的；不推荐省略花括号{}；多个if ... else串联要特别注意判断顺序；要注意if的边界条件；
-  要注意浮点数判断相等不能直接用==运算符；
- 引用类型判断内容相等要使用equals()，注意避免NullPointerException.
#### switch选择
- switch语句可以做多重选择，然后执行匹配的case语句后续代码；
- switch的计算结果必须是整型、字符串或枚举类型；
- 注意千万不要漏写break，建议打开fall-through警告；
- 总是写上default，建议打开missing default警告；
- 从Java 12开始，switch语句升级为表达式，不再需要break，并且代码更简洁.
####  while循环
- while循环先判断循环条件是否满足，再执行循环语句；
- while循环可能一次都不执行；
- 编写循环时要注意循环条件，并避免死循环.
#### do while循环
- do while循环先执行循环，再判断条件；
- do while循环会至少执行一次.
#### break和continue
- break语句可以跳出当前循环；
- break语句通常配合if，在满足条件时提前结束整个循环；
- break语句总是跳出最近的一层循环；
- continue语句可以提前结束本次循环；
- continue语句通常配合if，在满足条件时提前结束本次循环.
#### 数组
- 遍历数组可以使用for循环，for循环可以访问数组索引，for each循环直接迭代每个数组元素，但无法获取索引；
- 使用Arrays.toString()可以快速获取数组内容.
####  排序
- 常用的排序算法有冒泡排序、插入排序和快速排序等；
- 冒泡排序使用两层for循环实现排序；
- 交换两个变量的值需要借助一个临时变量。
- 可以直接使用Java标准库提供的Arrays.sort()进行排序；
- 对数组排序会直接修改数组本身.

#### 多维数组
- 二维数组就是数组的数组，三维数组就是二维数组的数组；
- 多维数组的每个数组元素长度都不要求相同；
- 打印多维数组可以使用Arrays.deepToString()；
- 最常见的多维数组是二维数组，访问二维数组的一个元素使用array[row][col].
#### 方法
- 方法可以让外部代码安全地访问实例字段；
- 方法是一组执行语句，并且可以执行任意逻辑；
- 方法内部遇到return时返回，void表示不返回任何值（注意和返回null不同）；
- 外部代码通过public方法操作实例，内部代码可以调用private方法；
- 理解方法的参数绑定.
#### 构造
- 实例在创建时通过new操作符会调用其对应的构造方法，构造方法用于初始化实例；
- 没有定义构造方法时，编译器会自动创建一个默认的无参数构造方法；
- 可以定义多个构造方法，编译器根据参数自动判断；
- 可以在一个构造方法内部调用另一个构造方法，便于代码复用.
#### 重载
- 方法重载是指多个方法的方法名相同，但各自的参数不同；
- 重载方法应该完成类似的功能，参考String的indexOf()；
- 重载方法返回值类型应该相同.
#### 继承
- 继承是面向对象编程的一种强大的代码复用方式；
- Java只允许单继承，所有类最终的根类是Object；
- protected允许子类访问父类的字段和方法；
- 子类的构造方法可以通过super()调用父类的构造方法；
- 可以安全地向上转型为更抽象的类型；
- 可以强制向下转型，最好借助instanceof判断；
- 子类和父类的关系是is，has关系不能用继承.

#### 多态
-  子类可以覆写父类的方法（Override），覆写在子类中改变了父类方法的行为；
-  Java的方法调用总是作用于运行期对象的实际类型，这种行为称为多态；
-  final修饰符有多种作用：
    -  final修饰的方法可以阻止被覆写；
    -  final修饰的class可以阻止被继承；
    -  final修饰的field必须在创建对象时初始化，随后不可修改.

#### 抽象类
- 通过abstract定义的方法是抽象方法，它只有定义，没有实现。抽象方法定义了子类必须实现的接口规范；
- 定义了抽象方法的class必须被定义为抽象类，从抽象类继承的子类必须实现抽象方法；
- 如果不实现抽象方法，则该子类仍是一个抽象类；
- 面向抽象编程使得调用者只关心抽象方法的定义，不关心子类的具体实现.

#### 接口
- Java的接口（interface）定义了纯抽象规范，一个类可以实现多个接口；
- 接口也是数据类型，适用于向上转型和向下转型；
- 接口的所有方法都是抽象方法，接口不能定义实例字段；
- 接口可以定义default方法（JDK>=1.8）.

#### 静态字段和静态方法
- 静态字段属于所有实例“共享”的字段，实际上是属于class的字段；
- 调用静态方法不需要实例，无法访问this，但可以访问静态字段和其他静态方法；
- 静态方法常用于工具类和辅助方法.

#### 包
- Java内建的package机制是为了避免class命名冲突；
- JDK的核心类使用java.lang包，编译器会自动导入；
- JDK的其它常用类定义在java.util.*，java.math.*，java.text.*，……；
- 包名推荐使用倒置的域名，例如org.apache.

#### 作用域
- Java内建的访问权限包括public、protected、private和package权限；
- Java在方法内部定义的变量是局部变量，局部变量的作用域从变量声明开始，到一个块结束；
- final修饰符不是访问权限，它可以修饰class、field和method；
- 一个.java文件只能包含一个public类，但可以包含多个非public类.

#### classpath与jar
- JVM通过环境变量classpath决定搜索class的路径和顺序；
- 不推荐设置系统环境变量classpath，始终建议通过-cp命令传入；
- jar包相当于目录，可以包含很多.class文件，方便下载和使用；
- MANIFEST.MF文件可以提供jar包的信息，如Main-Class，这样可以直接运行jar包.
### 核心类
#### 字符串与编码
- 当我们想要比较两个字符串是否相同时，要特别注意，我们实际上是想比较字符串的内容是否相同。必须使用equals()方法而不能用==，要忽略大小写比较，使用equalsIgnoreCase()方法

#### StringBuilder
- StringBuilder是可变对象，用来高效拼接字符串；
- StringBuilder可以支持链式操作，实现链式操作的关键是返回实例本身；
- StringBuffer是StringBuilder的线程安全版本，现在很少使用.
#### StringJoiner
- 用指定分隔符拼接字符串数组时，使用StringJoiner或者String.join()更方便；
- 用StringJoiner拼接字符串时，还可以额外附加一个“开头”和“结尾”.

#### 包装类型
- 基本类型：byte，short，int，long，boolean，float，double，char
- 引用类型：所有class和interface类型
- Java核心库提供的包装类型可以把基本类型包装为class；
- 自动装箱和自动拆箱都是在编译期完成的（JDK>=1.5）；
- 装箱和拆箱会影响执行效率，且拆箱时可能发生NullPointerException；
- 包装类型的比较必须使用equals()；
- 整数和浮点数的包装类型都继承自Number；
- 包装类型提供了大量实用方法.
#### JavaBean
- JavaBean是一种符合命名规范的class，它通过getter和setter来定义属性；
- 属性是一种通用的叫法，并非Java语法规定；
- 可以利用IDE快速生成getter和setter；
- 使用Introspector.getBeanInfo()可以获取属性列表
#### 枚举类
- 因此，引用类型比较，要始终使用equals()方法，但enum类型可以例外。
- 这是因为enum类型的每个常量在JVM中只有一个唯一实例，所以可以直接用==比较，
- Java使用enum定义枚举类型，它被编译器编译为final class Xxx extends Enum { … }；
- 通过name()获取常量定义的字符串，注意不要使用toString()；
- 通过ordinal()返回常量定义的顺序（无实质意义）；
- 可以为enum编写构造方法、字段和方法
- enum的构造方法要声明为private，字段强烈建议声明为final；
- enum适合用在switch语句中

#### BigInteger
- BigInteger用于表示任意大小的整数；
- BigInteger是不变类，并且继承自Number；
- 将BigInteger转换成基本类型时可使用longValueExact()等方法保证结果准确
#### BigDecimal
- BigDecimal用于表示精确的小数，常用于财务计算；
- 比较BigDecimal的值是否相等，必须使用compareTo()而不能使用equals()
#### 常用工具类
- Java提供的常用工具类有：
- Math：数学计算
- Random：生成伪随机数
- SecureRandom：生成安全的随机数

#### Java的异常
- Java使用异常来表示错误，并通过try ... catch捕获异常；
- Java的异常是class，并且从Throwable继承；
- Error是无需捕获的严重错误，Exception是应该捕获的可处理的错误；
- RuntimeException无需强制捕获，非RuntimeException（Checked Exception）需强制捕获，或者用throws声明；
- 不推荐捕获了异常但不进行任何处理。

#### 捕获异常
- 使用try ... catch ... finally时：
- 多个catch语句的匹配顺序非常重要，子类必须放在前面；
- finally语句保证了有无异常都会执行，它是可选的；
- 一个catch语句也可以匹配多个非继承关系的异常

#### 抛出异常
- 调用printStackTrace()可以打印异常的传播栈，对于调试非常有用；
- 捕获异常并再次抛出新的异常时，应该持有原始异常信息；
- 通常不要在finally中抛出异常。如果在finally中抛出异常，应该原始异常加入到原有异常中。调用方可通过Throwable.getSuppressed()获取所有添加的Suppressed Exception
#### 自定义异常
- 抛出异常时，尽量复用JDK已定义的异常类型；
- 自定义异常体系时，推荐从RuntimeException派生“根异常”，再派生出业务异常；
- 自定义异常时，应该提供多种构造方法
#### 断言
- 断言是一种调试方式，断言失败会抛出AssertionError，只能在开发和测试阶段启用断言；
- 对可恢复的错误不能使用断言，而应该抛出异常；
- 断言很少被使用，更好的方法是编写单元测试
#### 日志
- 日志是为了替代System.out.println()，可以定义格式，重定向到文件等；
- 日志可以存档，便于追踪问题；
- 日志记录可以按级别分类，便于打开或关闭某些级别；
- 可以根据配置文件调整日志，无需修改代码；
- Java标准库提供了java.util.logging来实现日志功能

### 反射
#### class类
- JVM为每个加载的class及interface创建了对应的Class实例来保存class及interface的所有信息；
- 获取一个class对应的Class实例后，就可以获取该class的所有信息；
- 通过Class实例获取class信息的方法称为反射（Reflection）；
- JVM总是动态加载class，可以在运行期根据条件来控制加载class。

#### 动态代理
- Java标准库提供了动态代理功能，允许在运行期动态创建一个接口的实例；
- 动态代理是通过Proxy创建代理对象，然后将接口方法“代理”给InvocationHandler完成的
#### 注解
- 注解（Annotation）是Java语言用于工具处理的标注：
- 注解可以配置参数，没有指定配置的参数使用默认值；

如果参数名称是value，且只有一个参数，那么可以省略参数名称
[廖雪峰Java](https://www.liaoxuefeng.com/wiki/1252599548343744/1255884132971296)
