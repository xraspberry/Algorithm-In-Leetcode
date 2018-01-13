import "fmt"

func hammingDistance(x int, y int) int {
	result := fmt.Sprintf("%b", x^y)
	count := 0
	for _, num := range result {
		if num == '1' {
			count += 1
		}
	}
	return count
}