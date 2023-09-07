# Higher Lower Game

Welcome to the Higher Lower Game! Test your intuition of Instagram followers count and see how high you can score. In this simple console-based game, you'll be presented with two options (Option A and Option B) and your task is to guess which of the two has more Instagram followers. The game keeps track of your score, and you'll receive feedback after each guess. Let's dive into the details of the game.

## Game Features

- **Game Logo**: A stylish game logo is displayed when you start the game to set the mood.

- **Two Options**: You'll be presented with two options, Option A and Option B, on the console. Each option includes the following information:
  - Person's Name
  - Short Description
  - The country they are associated with

- **Guess and Score**: After reviewing the information for both options, you will be prompted to make your guess about which of the two has more Instagram followers. If your guess is correct, you will receive a congratulatory message along with your updated score. If your guess is wrong, the game will end, and your final score will be displayed.

- **Option Rotation**:
  - After each guess, the game will clear the console.
  - Current option B becomes the next option A.
  - The game randomly selects the next option B.
  - Checks are in place to prevent the new Option B from being the same as the new Option A or the previous Option A.


## Game Data

The game data is stored in a list, which contains multiple dictionaries as its elements. Each dictionary includes the following information for an entity/person:
- Name
- Followers Count (Note: The followers count is not real-time and is stored as static data)
- Description
- Country

## How to Play

1. Clone this GitHub repository to your local machine.
2. Run the game script in your preferred Python environment.
3. Follow the on-screen instructions to make your guesses and enjoy the game!

## Contributing

If you'd like to contribute to this project or suggest improvements, please feel free to create a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code as long as you provide proper attribution and include the original license text.


