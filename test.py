import clogger

log = clogger.log('DEBUG', logger_name='test')
log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')
