import re
import operator

def operator_fn_by_char(op_char):
  operators = {
    '+': operator.add,
    '-': operator.sub
  }
  assert op_char in operators, "Error: Operator must be '+' or '-'."
  return operators[op_char]

def parse_problem(problem, should_sum):
  first_number, op, last_number = problem.split(' ')
  assert not re.search('[a-zA-Z]', first_number) , 'Error: Numbers must only contain digits.'
  assert not re.search('[a-zA-Z]', last_number) , 'Error: Numbers must only contain digits.'
  assert len(last_number) <= 4, 'Error: Numbers cannot be more than four digits.'
  
  operator_fn = operator_fn_by_char(op)
  line_1_len = len(first_number)
  line_2_len = len(last_number)
  chars_size = max(line_1_len, line_2_len)
  line_4 = ''

  if should_sum:
    op_result = operator_fn(int(first_number), int(last_number))
    op_result_str = str(op_result)
    op_result_size = len(op_result_str)
    chars_size = max(line_1_len, line_2_len, op_result_size - 1)
    line_4 = op_result_str.rjust(chars_size + 2)
  
  line_1 = first_number.rjust(chars_size + 2)
  line_2 = f'{op}{last_number.rjust(chars_size + 1)}'
  line_3 = '-' * (chars_size + 2)

  if should_sum:
      return [line_1, line_2, line_3, line_4]
  return [line_1, line_2, line_3]


def arithmetic_arranger(problems, should_sum=False):
    operations_matrix = None
  
    try:
      assert len(problems) <= 5, 'Error: Too many problems.'
      operations_matrix = list(
        map(
          lambda x: parse_problem(x, should_sum), 
          problems
        )
      )
    except Exception as e:
      return str(e)

    matrix_transposed = list(zip(*operations_matrix))
    values = ['    '.join(heads) for heads in matrix_transposed]
    arranged_problems = '\n'.join(values)
    return arranged_problems