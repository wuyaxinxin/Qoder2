// Package main 是程序的主包,包含了Person、Student和Calculator的示例实现
// 该程序展示了Go语言的基本特性,包括结构体、方法、错误处理等
package main

import (
	"fmt"  // 格式化输入输出包,用于打印和格式化字符串
	"time" // 时间处理包,用于获取和格式化时间
)

// Person 结构体表示一个人的基本信息
// 包含姓名、年龄和电子邮件三个字段
type Person struct {
	Name  string // 姓名
	Age   int    // 年龄
	Email string // 电子邮件地址
}

// NewPerson 创建一个新的Person实例
// 参数:
//   name - 姓名
//   age - 年龄
//   email - 电子邮件地址
// 返回:
//   *Person - 指向新创建的Person实例的指针
func NewPerson(name string, age int, email string) *Person {
	return &Person{
		Name:  name,
		Age:   age,
		Email: email,
	}
}

// String 方法返回Person的字符串表示
// 实现了Stringer接口,使Person对象可以被直接打印
// 返回:
//   string - 格式化后的人员信息字符串
func (p *Person) String() string {
	return fmt.Sprintf("Name: %s, Age: %d, Email: %s", p.Name, p.Age, p.Email)
}

// IsAdult 判断是否成年
// 根据年龄判断是否已满18岁
// 返回:
//   bool - 如果年龄>=18返回true,否则返回false
func (p *Person) IsAdult() bool {
	return p.Age >= 18
}

// Student 结构体继承Person的功能
// 通过嵌入Person结构体,Student获得了Person的所有字段和方法
// 同时添加了学生特有的学号和年级信息
type Student struct {
	Person           // 嵌入Person结构体,实现继承效果
	StudentID string // 学号
	Grade     int    // 年级
}

// NewStudent 创建一个新的Student实例
// 参数:
//   name - 学生姓名
//   age - 学生年龄
//   email - 学生电子邮件
//   studentID - 学号
//   grade - 年级
// 返回:
//   *Student - 指向新创建的Student实例的指针
func NewStudent(name string, age int, email string, studentID string, grade int) *Student {
	return &Student{
		Person: Person{
			Name:  name,
			Age:   age,
			Email: email,
		},
		StudentID: studentID,
		Grade:     grade,
	}
}

// String 方法返回Student的字符串表示
// 重写了Person的String方法,添加了学号和年级信息
// 返回:
//   string - 格式化后的学生信息字符串
func (s *Student) String() string {
	return fmt.Sprintf("Name: %s, Age: %d, Email: %s, StudentID: %s, Grade: %d",
		s.Name, s.Age, s.Email, s.StudentID, s.Grade)
}

// Calculator 计算器结构体
// 提供基本的四则运算功能,并记录计算历史
type Calculator struct {
	history []string // 保存计算历史记录的字符串切片
}

// NewCalculator 创建一个新的计算器
// 初始化一个空的历史记录切片
// 返回:
//   *Calculator - 指向新创建的Calculator实例的指针
func NewCalculator() *Calculator {
	return &Calculator{
		history: make([]string, 0), // 创建空的字符串切片
	}
}

// Add 加法运算
// 执行两个浮点数的加法,并将结果记录到历史中
// 参数:
//   a - 第一个加数
//   b - 第二个加数
// 返回:
//   float64 - 计算结果
func (c *Calculator) Add(a, b float64) float64 {
	result := a + b
	c.addToHistory(fmt.Sprintf("%.2f + %.2f = %.2f", a, b, result))
	return result
}

// Subtract 减法运算
// 执行两个浮点数的减法,并将结果记录到历史中
// 参数:
//   a - 被减数
//   b - 减数
// 返回:
//   float64 - 计算结果
func (c *Calculator) Subtract(a, b float64) float64 {
	result := a - b
	c.addToHistory(fmt.Sprintf("%.2f - %.2f = %.2f", a, b, result))
	return result
}

// Multiply 乘法运算
// 执行两个浮点数的乘法,并将结果记录到历史中
// 参数:
//   a - 第一个乘数
//   b - 第二个乘数
// 返回:
//   float64 - 计算结果
func (c *Calculator) Multiply(a, b float64) float64 {
	result := a * b
	c.addToHistory(fmt.Sprintf("%.2f * %.2f = %.2f", a, b, result))
	return result
}

// Divide 除法运算
// 执行两个浮点数的除法,并将结果记录到历史中
// 如果除数为0,则返回错误
// 参数:
//   a - 被除数
//   b - 除数
// 返回:
//   float64 - 计算结果
//   error - 如果除数为0,返回错误;否则返回nil
func (c *Calculator) Divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("除数不能为0") // 除数为0时返回错误
	}
	result := a / b
	c.addToHistory(fmt.Sprintf("%.2f / %.2f = %.2f", a, b, result))
	return result, nil
}

// addToHistory 添加计算历史
// 私有方法,用于将计算记录添加到历史切片中
// 参数:
//   record - 计算记录字符串
func (c *Calculator) addToHistory(record string) {
	c.history = append(c.history, record) // 将记录追加到历史切片
}

// GetHistory 获取计算历史
// 返回所有计算历史记录的副本
// 返回:
//   []string - 包含所有历史记录的字符串切片
func (c *Calculator) GetHistory() []string {
	return c.history
}

// ============================================
// 工具函数部分
// ============================================

// GetCurrentTime 获取当前时间的格式化字符串
// 使用Go的标准时间格式 "2006-01-02 15:04:05"
// 返回:
//   string - 格式化后的当前时间字符串
func GetCurrentTime() string {
	return time.Now().Format("2006-01-02 15:04:05") // Go的时间格式化布局
}

// Max 返回两个整数中的最大值
// 参数:
//   a - 第一个整数
//   b - 第二个整数
// 返回:
//   int - 两个整数中的较大值
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Min 返回两个整数中的最小值
// 参数:
//   a - 第一个整数
//   b - 第二个整数
// 返回:
//   int - 两个整数中的较小值
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// main 主函数
// 程序的入口点,展示了Person、Student、Calculator和工具函数的使用
func main() {
	// 打印程序标题和当前时间
	fmt.Println("=== Go 示例程序 ===")
	fmt.Println("当前时间:", GetCurrentTime())
	fmt.Println()

	// ========================================
	// Person示例:创建并测试Person实例
	// ========================================
	fmt.Println("--- Person 示例 ---")
	person := NewPerson("张三", 25, "zhangsan@example.com") // 创建Person对象
	fmt.Println(person)                                       // 打印Person信息
	fmt.Printf("%s 是否成年: %v\n", person.Name, person.IsAdult()) // 测试IsAdult方法
	fmt.Println()

	// ========================================
	// Student示例:创建并测试Student实例
	// ========================================
	fmt.Println("--- Student 示例 ---")
	student := NewStudent("李四", 20, "lisi@example.com", "S20230001", 3) // 创建Student对象
	fmt.Println(student)                                                  // 打印Student信息
	fmt.Printf("%s 是否成年: %v\n", student.Name, student.IsAdult())         // Student可以使用Person的方法
	fmt.Println()

	// ========================================
	// Calculator示例:测试四则运算和错误处理
	// ========================================
	fmt.Println("--- Calculator 示例 ---")
	calc := NewCalculator() // 创建计算器实例
	
	// 测试加法
	fmt.Printf("10 + 5 = %.2f\n", calc.Add(10, 5))
	// 测试减法
	fmt.Printf("10 - 5 = %.2f\n", calc.Subtract(10, 5))
	// 测试乘法
	fmt.Printf("10 * 5 = %.2f\n", calc.Multiply(10, 5))
	
	// 测试除法(正常情况)
	result, err := calc.Divide(10, 5)
	if err != nil {
		fmt.Println("错误:", err) // 处理错误
	} else {
		fmt.Printf("10 / 5 = %.2f\n", result)
	}

	// 测试除以0的情况(错误处理示例)
	_, err = calc.Divide(10, 0)
	if err != nil {
		fmt.Println("除以0错误:", err) // 捕获并显示除以0的错误
	}

	// 打印计算历史记录
	fmt.Println("\n计算历史:")
	for i, record := range calc.GetHistory() {
		fmt.Printf("%d. %s\n", i+1, record) // 遍历并显示每条历史记录
	}
	fmt.Println()

	// ========================================
	// 工具函数示例:测试Max和Min函数
	// ========================================
	fmt.Println("--- 工具函数示例 ---")
	fmt.Printf("Max(100, 50) = %d\n", Max(100, 50)) // 测试最大值函数
	fmt.Printf("Min(100, 50) = %d\n", Min(100, 50)) // 测试最小值函数
}
