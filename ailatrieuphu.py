import random

questions = [
    {
        "question": "Print() được sử dụng để làm gì trong Python?",
        "options": [
            "A. Nhập dữ liệu",
            "B. Xuất dữ liệu",
            "C. Tính toán",
            "D. Tạo biến",
        ],
        "correct_answer": "B",
    },
    {
        "question": "Đâu là cấu trúc điều kiện trong Python?",
        "options": ["A. for", "B. while", "C. if-elif-else", "D. print"],
        "correct_answer": "C",
    },
]
print("Chào mừng đến với trò chơi Ai Là Triệu Phú Python!")
score = 0
for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)

    answer = input("Nhập câu trả lời của bạn (A/B/C/D): ").upper()
    if answer == question["correct_answer"]:
        print("Chính xác!")
        score += 1
    else:
        print(f"Sai rồi. Đáp án đúng là {question['correct_answer']}.")

    print(f"Điểm số hiện tại: {score}\n")

print(f"Trò chơi kết thúc! Tổng điểm của bạn: {score}/{len(questions)}")
