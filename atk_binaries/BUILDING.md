# Example binaries

Shitty quick binaries to test the callers.

To build, do:

`for f in $(ls *.go); do go build $f; done`

Do that instead of just running 'go build' so that you don't have packages conflicting or requiring to have some specific directories.
