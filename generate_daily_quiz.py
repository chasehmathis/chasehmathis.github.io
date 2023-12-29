import random
import os
import pdb
# Load the template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Simple Quiz</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    margin: 20px;
  }}
  .question {{
    margin-bottom: 20px;
  }}
  .question h3 {{
    margin-bottom: 10px;
  }}
</style>
</head>
<body>
{content}
<script>
function submitAnswers() {{
  var totalQuestions = {total_questions}; // Update this with the actual number of questions
  var score = 0;

  // Check each question's answer
  {answer_checks}
  document.getElementById('result').textContent = "You scored " + score + "/" + totalQuestions;
}}
</script>

</body>
</html>
"""

# This is the HTML for a single quiz question
quiz_html = """
<div id="quiz">
  <div class="question">
    <h3>Question 1: What is 2 + 2?</h3>
    <input type="radio" id="q1a1" name="q1" value="3">
    <label for="q1a1">3</label><br>
    <input type="radio" id="q1a2" name="q1" value="4">
    <label for="q1a2">4</label><br>
    <input type="radio" id="q1a3" name="q1" value="5">
    <label for="q1a3">5</label>
  </div>
</div>
<button onclick="submitAnswers()">Submit</button>
<div id="result"></div>
"""

# Function to construct the answer check JavaScript
def construct_answer_check(question_number, correct_value):
    return f'var q{question_number} = document.querySelector(\'input[name="q{question_number}"]:checked\').value;\n  if(q{question_number} == \'{correct_value}\') score++;'

# Sample data - replace this with your actual data loading logic
today = random.sample(os.listdir('./submission'), 2)
questions = set(os.listdir('./problem'))
question_map = {}

for problem in today:
    id = problem.split('-')[0]

    txt_file = [x for x in questions if id in x][0]
    with open(f'./problem/{txt_file}', 'r') as f:
        problem_statement = f.read()  # Use read() to get the entire content as a single string

        question_map[id] = problem_statement

# Interleave the text and quizzes
full_content = ''
answer_checks = ''
question_number = 1

for id, problem_statement in question_map.items():
    full_content += f'<div>{problem_statement}</div>'  # Add the problem statement
    full_content += quiz_html.replace('Question 1', f'Question {question_number}')  # Add the quiz
    answer_checks += construct_answer_check(question_number, '4')  # Add the answer check
    question_number += 1

# Create the final HTML
final_html = template.format(content=full_content, total_questions=question_number - 1, answer_checks=answer_checks)

# Write the final HTML to a file
with open('./docs/PDF_Files/quiz.html', 'w') as file:
    file.write(final_html)
