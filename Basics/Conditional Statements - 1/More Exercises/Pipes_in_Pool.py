area = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
time = float(input())

first_pipe_total = pipe_1 * time
second_pipe_total = pipe_2 * time

total_filled = first_pipe_total + second_pipe_total
total_percentage = total_filled * 100 / area

first_in_perc = first_pipe_total * 100 / total_filled
second_in_perc = second_pipe_total * 100 / total_filled

difference = total_filled - area

if area >= total_filled:
    print(f"The pool is {total_percentage:.2f}% full. Pipe 1: {first_in_perc:.2f}%. Pipe 2: {second_in_perc:.2f}%.")
elif area < total_filled:
    print(f"For {time} hours the pool overflows with {difference:.2f} liters.")
