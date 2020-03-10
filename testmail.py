import logging.handlers

def sendMail():
	error_mail_subject = "Server Overload"
	error_mail_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587),
	                                              fromaddr="testmail.sio22@gmail.com",
	                                              toaddrs="yahialamri.pro@gmail.com",                                                  
	                                              subject=error_mail_subject,
	                                              credentials=('testmail.sio22@gmail.com', 'testmail'),
	                                              secure=())
	error_mail_handler.setLevel(logging.ERROR)
	logger = logging.getLogger()
	logger.addHandler(error_mail_handler)
	logger.exception(Exception("OULALA C TOUT CASSE"))