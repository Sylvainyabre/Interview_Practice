package main

import (
	"fmt"
	"time"
)

type Person struct {
	First    string
	Last     string
	Email    string
	BirthDay time.Time
	School   School
}
type School struct {
	Name    string
	Country string
}

func (sc School) Yell() {
	fmt.Printf("I am %v located in %v \n", sc.Name, sc.Country)
}

func NewPerson(first string, last string, email string, birthdate string) (p *Person) {
	date, _ := time.Parse(`"2006-01-02"`, birthdate)
	return &Person{
		First:    first,
		Last:     last,
		Email:    email,
		BirthDay: date,
		School: School{
			Name:    "UBC",
			Country: "Canada",
		},
	}

}
func (person Person) IntroduceSelf() {
	fmt.Print("Hello World \n")
	fmt.Printf("My name is %v %v \n", person.First, person.Last)
	fmt.Printf("My email address is %v \n", person.Email)
	fmt.Printf("I was borned on %v \n", person.BirthDay)
}
func main() {
	newPerson := NewPerson("Sylvain", "Yabre", "yabre@student.ubc.ca", "1999/12/31")
	newPerson.IntroduceSelf()
	newPerson.School.Yell()
	fmt.Println("hello World")
}

// create a function to determine if two strings are anagrams
