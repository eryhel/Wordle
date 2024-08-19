# Wordle Game in Python

#### <a href="https://www.youtube.com/watch?v=W8EhOMBUqzE">Video Demo</a>

#### Description:

This project is a command-line implementation of the popular word-guessing game, Wordle. The game challenges players to guess a randomly selected five-letter word within six attempts. Each guess provides feedback on the accuracy of the letters in the guess, using color-coded hints to indicate whether a letter is in the correct position, is in the word but in the wrong position, or is not in the word at all.

### How It Works:
- The game begins by selecting a random five-letter word from a list stored in a text file (`words.txt`).
- The player is then prompted to input a five-letter word as their guess. The guess is compared to the target word, and feedback is provided:
  - **Green** indicates the letter is in the correct position.
  - **Yellow** indicates the letter is in the word but in the wrong position.
  - **Red** indicates the letter is not in the word at all.
- The player has six attempts to guess the correct word. If they succeed, a congratulatory message is displayed. If they fail to guess the word within the allotted attempts, the correct word is revealed.

### Files:
- **`project.py`**: This is the main file that contains the game logic. It handles the word selection, user input, feedback generation, and displays the results. Key functions include:
  - `get_random_word(path)`: Retrieves a random word from the provided file.
  - `check_guess(word, guess)`: Checks if the guess is correct.
  - `print_results(attempts, word)`: Displays the results after each guess, using color-coded hints.
- **`words.txt`**: A text file containing a list of possible words for the game. This file is essential for selecting a random word for the player to guess.
- **`test_project.py`**: A file containing unit tests for the game, using the `pytest` framework. It includes tests for:
  - `test_check_guess_false()`: Verifies that incorrect guesses are handled correctly.
  - `test_check_guess_true()`: Verifies that correct guesses are recognized.
  - `test_get_random_word()`: Ensures that the word retrieval function raises an error when the word file is not found.


### How to Use:

1. **Clone the Repository**:
   - First, clone the repository to your local machine using the following command:
   
   ```bash
   git clone <REPOSITORY_URL>
   ```

   Replace <REPOSITORY_URL> with the actual URL of your repository.

2. **Navigate to the Project Directory**:
   - Move into the project directory:
   
   ```bash
   cd <project-directory>
   ```

3. **Install the Dependencies**:
   - Install the required Python packages by running:
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**:
   - Start the game by executing the following command:
   
   ```bash
   python project.py
   ```

   The game will launch, and you can begin playing by following the on-screen instructions.

5. **Run Tests**:
   - To run the tests for the project, execute:
   
   ```bash
   pytest test_project.py
   ```

   This will run the unit tests to ensure the game functions correctly.


### Design Choices:
One of the key design decisions was to use color-coded output to provide feedback to the player, which enhances the user experience by making it visually clear how close the guess was to the correct word. The game logic was kept simple and modular, with each function handling a specific task, making the code easy to read and maintain.

I also implemented error handling for scenarios where the word list file is missing or empty, ensuring the game exits gracefully with a meaningful error message. Additionally, the game enforces input validation, requiring that the player’s guess be a valid five-letter word.

### Future Enhancements:
- **Improved Word List**: Currently, the word list is static and limited. Future improvements could include a larger, more dynamic word list or an API to fetch new words.
- **Graphical Interface**: While the current implementation is command-line based, adding a graphical user interface (GUI) could make the game more engaging and accessible.
- **Leaderboard**: Implementing a leaderboard to track players' scores and compare them could add a competitive element to the game.

This project showcases fundamental Python programming skills, including file handling, string manipulation, user input, and basic error handling. It also demonstrates the use of color-coded terminal output to enhance user interaction, providing a satisfying and challenging game experience.
