func addNumbers(_ numbers: Int...) -> Int {
    return numbers.reduce(0, +)
}

// Example usage
let sum = addNumbers(1, 2, 3, 4, 5)
print("The sum is: \(sum)")
