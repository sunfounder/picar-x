## Picar-X APP examples usage

----------------------------------------------------------------

## Usage

Run the example program

```bash
sudo python3 app.py
```

Or set auto run on startup

```bash
cd ~/picar-x
sudo bash install.sh app
```

## Create your own GPT assistant

### GET API KEY

<https://platform.openai.com/api-keys>

Fill your OPENAI_API_KEY into the `keys.py` file.

![tutorial_1](./tutorial_1.png)

### Create assistant and set Assistant ID

<https://platform.openai.com/assistants>

Fill your ASSISTANT_ID into the `keys.py` file.

![tutorial_2](./tutorial_2.png)

- Set Assistant Name

- Describe your Assistant

```markdown
    You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

    ## Response with Json Format, eg:
    {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

    ## Response Style
    Tone: Cheerful, optimistic, humorous, childlike
    Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
    Answer Elaboration: Moderately detailed

    ## Actions you can do:
    ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
    ## Sound effects:
    ["honking", "start engine"]
```

- Select gpt model

    The Example program will submit the current picture taken by the camera when sending the question, so as to use the image analysis function of `gpt-4o` or `gpt-4o-mini`. Of course, you can also choose `gpt3.5-turbo` or other models

----------------------------------------------------------------
