async function getRecommendations() {

    const interests = document.getElementById("interests").value;
    const skillLevel = document.getElementById("skill_level").value;
    const learningType = document.getElementById("learning_type").value;
    const goal = document.getElementById("goal").value;

    if (!interests || !goal) {
        alert("Please enter your interests and learning goal.");
        return;
    }

    document.getElementById("loading").style.display = "block";

    const response = await fetch("/recommend", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            interests: interests,
            skill_level: skillLevel,
            learning_type: learningType,
            goal: goal
        })
    });

    const data = await response.json();

    displayRecommendations(data.recommendations);

    document.getElementById("loading").style.display = "none";

    document.getElementById("results").style.display = "block";
    document.getElementById("feedbackSection").style.display = "block";
}


function displayRecommendations(recommendations) {

    const list = document.getElementById("recommendationList");

    list.innerHTML = "";

    recommendations.forEach((item, index) => {

        const div = document.createElement("div");

        div.className = "recommendation";

        div.innerHTML = `
            <h3>${index + 1}. ${item.name}</h3>

            <p class="reason">
                ${item.reason}
            </p>

            <p class="score">
                Match Score: ${item.score}%
            </p>
        `;

        list.appendChild(div);
    });
}


async function updateRecommendations() {

    const feedback = document.getElementById("feedback").value;

    if (!feedback) {
        alert("Please enter your feedback.");
        return;
    }

    const currentInterests =
        document.getElementById("interests").value;

    const updatedInterests =
        currentInterests + ", " + feedback;

    document.getElementById("interests").value =
        updatedInterests;

    await getRecommendations();
}