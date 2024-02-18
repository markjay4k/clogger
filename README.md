# CLOGGER

A simple python logger with a funny name

## FEATURES

- Rotating logfiles
- Loglevel colors
- Aligned module names
- Additional `mods` dataclass for adding colors to text

## USAGE

```python
    import clogger

    log = clogger.log('DEBUG', logger_name='test')
    log.debug('debug message')
    log.info('info message')
    log.warning('warning message')
    log.error('error message')
    log.critical('critical message')
```

And the output 

```bash
    2024-02-18 19:03:25| [36;20m[1m   test[0m[0m [36;20m   DEBUG[0m| debug message
    2024-02-18 19:03:25| [36;20m[1m   test[0m[0m [32;20m    INFO[0m| info message
    2024-02-18 19:03:25| [36;20m[1m   test[0m[0m [33;20m WARNING[0m| warning message
    2024-02-18 19:03:25| [36;20m[1m   test[0m[0m [31;20m   ERROR[0m| error message
    2024-02-18 19:03:25| [36;20m[1m   test[0m[0m [31;1mCRITICAL[0m| critical message
```
