SELECT SUM(win) AS total_win, SUM(loss) AS total_loss, SUM(tie) AS total_tie
FROM blackjack
WHERE name <> 'Dealer';

SELECT SUM(win) AS total_win, SUM(loss) AS total_loss, SUM(tie) AS total_tie
FROM blackjack
WHERE name = 'Dealer';