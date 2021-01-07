package main

import "fmt"

type contactInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	// contact   contactInfo
	contactInfo
}

func main() {
	// alex := person{firstName: "Alex", lastName: "Anderson"}
	// fmt.Println(alex)

	// var alex person
	// alex.firstName = "Alex"
	// alex.lastName = "Anderson"

	// fmt.Println(alex)
	// fmt.Printf("%+v", alex)

	jim := person{
		firstName: "Jim",
		lastName:  "Party",
		contactInfo: contactInfo{
			email:   "jim@gmail.com",
			zipCode: 94000,
		},
		// contact: contactInfo{
		// 	email:   "jim@gmail.com",
		// 	zipCode: 94000,
		// },
	}

	// jimPointer := &jim // give me the memory address of the value this variable is pointing at
	// jimPointer.updateName("Jimmy")
	jim.updateName("Jimmy")
	jim.print()
}

func (pointerToPerson *person) updateName(newFirstName string) { // we are working with a pointer to a person
	(*pointerToPerson).firstName = newFirstName // we want to manipulate the value the point is referencing
}

func (p person) print() {
	fmt.Printf("%+v", p)
}
