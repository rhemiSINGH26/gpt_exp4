from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def generate_recommendations(interests, skill_level, learning_type, goal):
    interests = interests.lower()
    skill_level = skill_level.lower()
    learning_type = learning_type.lower()
    goal = goal.lower()

    recommendations = []

    # Java
    if "java" in interests or "java" in goal:
        recommendations.extend([
            {
                "name": "Java Programming Fundamentals",
                "reason": "Builds a strong foundation in Java programming.",
                "score": 95
            },
            {
                "name": "Object-Oriented Programming with Java",
                "reason": "Helps understand important Java OOP concepts.",
                "score": 92
            },
            {
                "name": "Java Data Structures",
                "reason": "Improves programming and problem-solving skills.",
                "score": 88
            },
            {
                "name": "Java Mini Projects",
                "reason": "Provides hands-on practical Java experience.",
                "score": 86
            },
            {
                "name": "Spring Boot Development",
                "reason": "Helps build real-world Java applications.",
                "score": 82
            }
        ])

    # AI
    if "ai" in interests or "artificial intelligence" in interests:
        recommendations.extend([
            {
                "name": "Artificial Intelligence Fundamentals",
                "reason": "Matches your interest in Artificial Intelligence.",
                "score": 95
            },
            {
                "name": "Machine Learning Basics",
                "reason": "Provides a foundation for learning AI.",
                "score": 92
            },
            {
                "name": "Generative AI",
                "reason": "Introduces modern AI and language-model concepts.",
                "score": 90
            },
            {
                "name": "Deep Learning Fundamentals",
                "reason": "Provides a natural progression after Machine Learning.",
                "score": 87
            },
            {
                "name": "Computer Vision",
                "reason": "Introduces practical AI applications using images.",
                "score": 84
            }
        ])

    # Python
    if "python" in interests or "python" in goal:
        recommendations.extend([
            {
                "name": "Python Programming",
                "reason": "Matches your interest in Python programming.",
                "score": 95
            },
            {
                "name": "Python for Data Science",
                "reason": "Combines Python programming with data analysis.",
                "score": 91
            },
            {
                "name": "Machine Learning with Python",
                "reason": "Provides practical AI experience using Python.",
                "score": 89
            }
        ])

    # Cybersecurity
    if "cybersecurity" in interests or "security" in interests:
        recommendations.extend([
            {
                "name": "Cybersecurity Fundamentals",
                "reason": "Matches your cybersecurity interest.",
                "score": 95
            },
            {
                "name": "Network Security",
                "reason": "Builds important security knowledge.",
                "score": 92
            },
            {
                "name": "Ethical Hacking Fundamentals",
                "reason": "Introduces practical cybersecurity concepts.",
                "score": 89
            }
        ])

    # Web Development
    if "web" in interests:
        recommendations.extend([
            {
                "name": "HTML and CSS",
                "reason": "Builds the foundation for web development.",
                "score": 94
            },
            {
                "name": "JavaScript Programming",
                "reason": "Adds programming skills for web applications.",
                "score": 91
            },
            {
                "name": "Full Stack Development",
                "reason": "Combines frontend and backend development.",
                "score": 88
            }
        ])

    # Default recommendations
    if not recommendations:
        recommendations = [
            {
                "name": "Programming Fundamentals",
                "reason": "Builds a strong computer science foundation.",
                "score": 90
            },
            {
                "name": "Python Programming",
                "reason": "A versatile programming language.",
                "score": 88
            },
            {
                "name": "Data Structures",
                "reason": "Improves programming and problem-solving skills.",
                "score": 85
            },
            {
                "name": "Artificial Intelligence Fundamentals",
                "reason": "Introduces modern AI concepts.",
                "score": 82
            },
            {
                "name": "Practical Programming Projects",
                "reason": "Provides hands-on programming experience.",
                "score": 80
            }
        ]

    # Remove duplicates
    unique = []
    seen = set()

    for item in recommendations:
        if item["name"] not in seen:
            unique.append(item)
            seen.add(item["name"])

    # Sort by score
    unique.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return unique[:5]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    recommendations = generate_recommendations(
        data.get("interests", ""),
        data.get("skill_level", ""),
        data.get("learning_type", ""),
        data.get("goal", "")
    )

    return jsonify({
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(debug=True)