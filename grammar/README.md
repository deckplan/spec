# Grammar
This file defines the grammars for:
1. The Substrait Type language used in the YAML extensions.
2. The test grammar language used to unit tests functions.

## Regenerating
To regenerate all of the parsers use the following command
```sh
make all
```

### Requirements
You will need [ANTLR](https://www.antlr.org/index.html) available on your machine to regenerate the parser.

#### MacOS
```
brew install antlr
```

#### Ubuntu
```
sudo apt-get install antlr4
```