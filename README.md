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
    2024-02-18 19:03:25|    test    DEBUG| debug message
    2024-02-18 19:03:25|    test     INFO| info message
    2024-02-18 19:03:25|    test  WARNING| warning message
    2024-02-18 19:03:25|    test    ERROR| error message
    2024-02-18 19:03:25|    test CRITICAL| critical message
```
