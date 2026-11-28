# class Messenger:
    # def send_message (self):
        # print("Text messge is sent")
    # def receive_message (self) :
        # print("Text messe is receive")
# class InternalMessenger (Messenger):
    # pass
# class WhatsappMessenger:
    # def send_message (self):
        # print("Text, Photos, Videos & Files is sent")
    # def receive_message (self) :
        # ("Text, Photos, Videos & Files is received")
    # def set_dp (self):
        # print("DP is set")
    # def set_status(self):
        # print ("Status is set")
# Im = InternalMessenger()
# Im.send_message()
# Im.receive_message()      #inheridance,overridden,specilized(methods)


#class Messenger:
    #def use_keyboard(self):
       # print("Using keyboard")
    #def send_message(self):
      #  print("Text message sent")
    #def receive_message(self):
      #  print("Text message received")

#class WhatsApp(Messenger):
    #def send_message(self):
       # print("Text, video and audio sent using WhatsApp")
    #def receive_message(self):
       # print("Text, video and audio received using WhatsApp")
    #def send_live_location(self):
       # print("Live location sent using WhatsApp")

#class FacebookMessenger(Messenger):
    #def send_message(self):
        #print("Text, video and audio sent using Facebook")
    #def receive_message(self):
     #   print("Text, video and audio received using Facebook")
   # def use_builtin_apps(self):
       # print("Using built-in apps in Facebook Messenger")

#class InstagramMessenger(Messenger):
    #def send_message(self):
       # print("Text, video and audio sent using Instagram")
    #def receive_message(self):
       # print("Text, video and audio received using Instagram")
    #def add_filters(self):
       # print("Filters applied using Instagram")

#def use_messenger(ref):
    # ref.use_keyboard()
    # ref.send_message()
    # ref.receive_message()
   # if isinstance(ref, WhatsApp):
      #  ref.send_live_location()
    #elif isinstance(ref, FacebookMessenger):
      #  ref.use_builtin_apps()
   # elif isinstance(ref, InstagramMessenger):
       # ref.add_filters()

# wa = WhatsApp()
# fb = FacebookMessenger()
# insta = InstagramMessenger()
# use_messenger(wa)
# use_messenger(fb)
# use_messenger(insta)    #hirachical inheridance or polymorphism method


     
