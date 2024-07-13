
# 🎮 Tic Tac Toe with Minimax Algorithm 🧠

**Course:** Artificial Intelligence (Game Theory Topic)  
**Program:** MSc. Intelligent Computer Systems Engineering  
**Author:** Shyaka Noble David

![Tic Tac Toe](https://img.icons8.com/color/48/000000/tic-tac-toe.png)

---

## 🌟 Overview

This project is a web-based Tic Tac Toe game implemented using Flask and the Minimax algorithm. It is part of the Artificial Intelligence course under the Game Theory topic in fulfillment of the MSc. Intelligent Computer Systems Engineering.

The Minimax algorithm is used to create an unbeatable AI opponent, ensuring a challenging experience for players.

---

## 🚀 Features

- **Unbeatable AI**: The AI uses the Minimax algorithm to always make the optimal move.
- **User-Friendly Interface**: Simple and intuitive design for a seamless gaming experience.
- **New Game Option**: Easily start a new game at any time.

---

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/tic_tac_toe_minimax.git
    cd tic_tac_toe_minimax
    ```

2. **Install dependencies**:
    ```bash
    pip install flask
    ```

3. **Run the application**:
    ```bash
    python tic_tac_toe.py
    ```

4. **Open your browser and navigate to**: 
    ```
    http://127.0.0.1:5000/
    ```

---

## 🕹️ How to Play

1. **Enter your move**: Specify your move in the format `row,column` (e.g., `1,1` for the top-left corner).
2. **Submit**: Click the submit button to make your move.
3. **AI's Turn**: The AI will make its move automatically.
4. **Game Over**: The game will display the result (win/lose/tie) and allow you to start a new game.

---

## 📋 Code Structure

- **`tic_tac_toe.py`**: Main application file containing the Flask app and Minimax algorithm.
- **`templates/index.html`**: HTML template for the game interface.

---

## ✨ Screenshots

![Game Interface](screenshot.png)

---

## 📚 Learning Outcomes

- Understanding of the Minimax algorithm and its application in Game Theory.
- Experience with Flask for web development.
- Improved problem-solving and algorithmic thinking skills.

---

## 🎨 Styling

To make the game more visually appealing, consider adding some CSS to the `index.html` file:

```css
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
}

h1 {
    color: #333;
}

.board {
    display: inline-block;
    border: 2px solid #333;
}

.row {
    display: flex;
}

.cell {
    width: 60px;
    height: 60px;
    border: 1px solid #333;
    line-height: 60px;
    font-size: 24px;
    cursor: pointer;
}

.message {
    margin-top: 20px;
    font-size: 18px;
    color: #555;
}
```

---

## 📝 License

This project is licensed under the MIT License.

---

Feel free to reach out if you have any questions or need further assistance!

Happy coding! 🚀

---

Enjoy playing and exploring the fascinating world of Game Theory and Artificial Intelligence! 🌟
