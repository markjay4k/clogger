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
