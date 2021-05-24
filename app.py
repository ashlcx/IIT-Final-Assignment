"""
Copyright 2021 Ashley Hines

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys

## Cant use tuple or array as negative will call nth value
C_INT_RANGE = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:8, 10:10} 

def main(strInput: str) -> Exception:
    try:
        iInput = int(strInput)  ## Type Exception not int (ValueError)
        iValue = C_INT_RANGE.get(iInput)  ## Tuple Out of bounds Exception (IndexError)
        fResult = 1 / iValue  ## Divide by zero Exception (ZeroDivisionError)
        ## Once made this far, print result in
        print("The Reciprocal of your number is {}".format(fResult))
        ## Exceptions
        return True
    except ValueError:  ## Called if strInput cannot be cast into an int
        raise ValueError("You did not enter an integer!!!")
    except ZeroDivisionError: ## Called when zero is entered
        raise ZeroDivisionError("Oops, you entered zero.")
    except TypeError: ## Called when number < 0 & > 10
        raise TypeError("You did not enter a number between 1 and 10!!!")
    except Exception as e: ## This should never be called, will print out other exceptions
        raise e


## Allows code to be imported as a library without running
if __name__ == "__main__":
    ## Call main function
    while True:
        strInput = input("Enter an integer between 1 to 10: ")
        try:
            res = main(strInput)
            if type(res) is bool:
                break
        except Exception as e:
            print(e)
    ## Exit with code 0
    sys.exit(0)
