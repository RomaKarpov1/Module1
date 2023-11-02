def sort_by_mean(array):
  means = []
  for i in range(len(array[0])):
    mean = 0
    for j in range(len(array)):
      mean += array[j][i]
    means.append(mean / len(array))
  sorted_indices = sorted(range(len(means)), key=lambda i: means[i])
  sorted_array = []
  for i in sorted_indices:
    sorted_array.append([row[i] for row in array])

  return sorted_array
def main():
  array = []
  n = int(input("Введіть розмір масиву: "))
  for i in range(n):
    numbers = input("Введіть числа для рядка {}: ".format(i + 1))
    row = [int(number) for number in numbers.split()]
    array.append(row)

  sorted_array = sort_by_mean(array)

  print(sorted_array)


if __name__ == "__main__":
  main()
