package files

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
)

func ReadFile(fileName string) {

	fmt.Printf("\n\nReading a file in Go lang\n")

	// The ioutil package contains inbuilt
	// methods like ReadFile that reads the
	// filename and returns the contents.
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}

	fmt.Printf("\nData: %s", data)

}

func ReadFileBuffer(fileName string) []int {
	// os.Open() opens specific file in
	// read-only mode and this return
	// a pointer of type os.
	file, err := os.Open(fileName)

	if err != nil {
		log.Fatalf("failed to open")

	}

	// The bufio.NewScanner() function is called in which the
	// object os.File passed as its parameter and this returns a
	// object bufio.Scanner which is further used on the
	// bufio.Scanner.Split() method.
	scanner := bufio.NewScanner(file)

	// The bufio.ScanLines is used as an
	// input to the method bufio.Scanner.Split()
	// and then the scanning forwards to each
	// new line using the bufio.Scanner.Scan()
	// method.
	scanner.Split(bufio.ScanLines)
	var resp []int

	for scanner.Scan() {
		text, _ := strconv.Atoi(scanner.Text())
		resp = append(resp, text)
	}

	// The method os.File.Close() is called
	// on the os.File object to close the file
	file.Close()

	return resp
}
