# Simple cli client for ja.is

Personal tool that is probably not useful for anyone else

## Install

```bash
pip install jais-search
```

## Play around

Start by exporting your api token

```bash
export JAIS_API_KEY=your-token
```

Alternatively you can always pass it as an argument to each command, but that's just boring

```bash
jais search --token your-token -n "Code"
```

The token will be inferred from your environment
```bash
jais search -n "Code"
```

![image](https://user-images.githubusercontent.com/3162968/236763732-5f8b8ba4-3541-46c6-aff4-93272f2ae06f.png)

Only one command is available, that is `search`, but comes with multiple search filter options.

```bash
jais search --help
```
![image](https://user-images.githubusercontent.com/3162968/236764546-714e9f32-f97e-477b-9230-e37ee91e0747.png)

### Search examples

```bash
jais search -n "Banana"
jais search -p 105 # postal code
jais search -s  Suðurlandsbraut # street
jais search -m  Reykjavík # municipality
jais search -b  E1 # business type, I have no idea what codes are available.
```

Or just pass them all in if you want

```bash
jais search -n "Banana" -p 105 -s  Suðurlandsbraut -m  Reykjavík municipality -b  E1
```

It will store results in `test.csv`, until I make it configurable and fix the dict serialization.

The https://ja.is api paginates the data so you have to pass in `--start [default: 1]` and `--count [default: 1000]`, but it comes with defaults.

```bash
# Get me 50 records and start at record 1000
jais search -n "Banana" --start 1000 --count 50
```
