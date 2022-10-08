let a = 1;
let b = 10;
let secret_number = Math.round(a + (b - a) * Math.random());
guessed_number = parseInt(prompt("Enter your guess"))


function game() {
    let guess = 1;
    while (guess <= 3) {

        if (guessed_number == secret_number) {
            alert("You have guessd the number!!");
            return
        }
        else if (guess == 3) {
            alert("You have failed");
            return;
        }
        else {
            guessed_number = parseInt(prompt("Try again"))
        }

        guess++;
    }
}
game()