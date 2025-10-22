package main

import (
	"fmt"
	"time"
)

// Person 结构体表示一个人的基本信息
type Person struct {
	Name string
	Age  int
	Email string
}

// NewPerson 创建一个新的Person实例
func NewPerson(name string, age int, email string) *Person {
	return &Person{
		Name:  name,
		Age:   age,
		Email: email,
	}
}

// String 方法返回Person的字符串表示
func (p *Person) String() string {
	return fmt.Sprintf("Name: %s, Age: %d, Email: %s", p.Name, p.Age, p.Email)
}

// IsAdult 判断是否成年
func (p *Person) IsAdult() bool {
	return p.Age >= 18
}

// Student 结构体继承Person的功能
type Student struct {
	Person
	StudentID string
	Grade     int
}

// NewStudent 创建一个新的Student实例
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
func (s *Student) String() string {
	return fmt.Sprintf("Name: %s, Age: %d, Email: %s, StudentID: %s, Grade: %d",
		s.Name, s.Age, s.Email, s.StudentID, s.Grade)
}

// Calculator 计算器结构体
type Calculator struct {
	history []string
}

// NewCalculator 创建一个新的计算器
func NewCalculator() *Calculator {
	return &Calculator{
		history: make([]string, 0),
	}
}

// Add 加法运算
func (c *Calculator) Add(a, b float64) float64 {
	result := a + b
	c.addToHistory(fmt.Sprintf("%.2f + %.2f = %.2f", a, b, result))
	return result
}

// Subtract 减法运算
func (c *Calculator) Subtract(a, b float64) float64 {
	result := a - b
	c.addToHistory(fmt.Sprintf("%.2f - %.2f = %.2f", a, b, result))
	return result
}

// Multiply 乘法运算
func (c *Calculator) Multiply(a, b float64) float64 {
	result := a * b
	c.addToHistory(fmt.Sprintf("%.2f * %.2f = %.2f", a, b, result))
	return result
}

// Divide 除法运算
func (c *Calculator) Divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("除数不能为0")
	}
	result := a / b
	c.addToHistory(fmt.Sprintf("%.2f / %.2f = %.2f", a, b, result))
	return result, nil
}

// addToHistory 添加计算历史
func (c *Calculator) addToHistory(record string) {
	c.history = append(c.history, record)
}

// GetHistory 获取计算历史
func (c *Calculator) GetHistory() []string {
	return c.history
}

// 工具函数

// GetCurrentTime 获取当前时间的格式化字符串
func GetCurrentTime() string {
	return time.Now().Format("2006-01-02 15:04:05")
}

// Max 返回两个整数中的最大值
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Min 返回两个整数中的最小值
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// main 主函数
func main() {
	fmt.Println("=== Go 示例程序 ===")
	fmt.Println("当前时间:", GetCurrentTime())
	fmt.Println()

	// 创建Person实例
	fmt.Println("--- Person 示例 ---")
	person := NewPerson("张三", 25, "zhangsan@example.com")
	fmt.Println(person)
	fmt.Printf("%s 是否成年: %v\n", person.Name, person.IsAdult())
	fmt.Println()

	// 创建Student实例
	fmt.Println("--- Student 示例 ---")
	student := NewStudent("李四", 20, "lisi@example.com", "S20230001", 3)
	fmt.Println(student)
	fmt.Printf("%s 是否成年: %v\n", student.Name, student.IsAdult())
	fmt.Println()

	// 计算器示例
	fmt.Println("--- Calculator 示例 ---")
	calc := NewCalculator()
	fmt.Printf("10 + 5 = %.2f\n", calc.Add(10, 5))
	fmt.Printf("10 - 5 = %.2f\n", calc.Subtract(10, 5))
	fmt.Printf("10 * 5 = %.2f\n", calc.Multiply(10, 5))
	
	result, err := calc.Divide(10, 5)
	if err != nil {
		fmt.Println("错误:", err)
	} else {
		fmt.Printf("10 / 5 = %.2f\n", result)
	}

	// 测试除以0的情况
	_, err = calc.Divide(10, 0)
	if err != nil {
		fmt.Println("除以0错误:", err)
	}

	fmt.Println("\n计算历史:")
	for i, record := range calc.GetHistory() {
		fmt.Printf("%d. %s\n", i+1, record)
	}
	fmt.Println()

	// 工具函数示例
	fmt.Println("--- 工具函数示例 ---")
	fmt.Printf("Max(100, 50) = %d\n", Max(100, 50))
	fmt.Printf("Min(100, 50) = %d\n", Min(100, 50))
}
