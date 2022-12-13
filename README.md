# Rock, paper scissors -- the web app
> Because you can never have enough screen time!

- [How to play in the real world](https://en.wikipedia.org/wiki/Rock_paper_scissors)
- [How to play using this web app](#Run)

## Strategy: ##
> I pledged early on to restrict myself to the 3-hour time limit at the risk of seeming less efficient than developers who didn't.  I wrote this strategy to keep myself on track.  (Conf)

The prompt for user input in the web, backend logic, and the ability to save seems like an impossible task in 3 hours. 

### Priorities ###
1. Working code for logic 
2. A working web app ("in the web browser")
3. Documentation
4. Working database for the web app to store games
5. Unit tests
6. Security (this should be #1, but I determined the info saved to be non-sensitive)
7. Deployability 

## Personal challenges: ##
> The effort that isn't reflected in my code
1.  I had to re-learn Flask, which I hadn't used > 4 years, but wanted to showcase my Python skills.
     - The prompt said code had to be displayed in the web browser
     - AWS seems too specialized for a code challenge plus I don't have an AWS account
2.  GitHub problems.

## How I cheated ##
While I was setting up Gitlab, I noticed  the Codespace and used this to develop and save my code.

## What I would do if I had more time ##
1. If I had another hour (I'd do one or more of the following):
- get session code to work
- add logic to save session["game"] to dictionary
- (probably not enough time)
- add logic for autogenerate moves

2.  if I had another 3 hours;
- official unit tests and smokescreen tests

3.  If I had another 3 days:
- update game.py to be a model, dockerize, use a postgres database to save
output
- add deployment scripts
- associate session with login/auth

## Run ##
1. Got to [rock-paper-scissors codespace](https://erica-snake-case-super-duper-rotary-phone-977gw57v565fqjg.github.dev/)

2.  Be sure to navigate to http://127.0.0.1:5000 because the session won't work in the preview (learned that one the hard way)

