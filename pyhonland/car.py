class Car:
    speed = 0
    started = False

    def start(context):
        context.started = True
        print("Car started, let's go")

    def increase_speed(context, delta):
        if context.started:
            context.speed += delta
            print('Vroooooom!')
        else:
            print('Start your Car')
    
    def stop(context):
        context.start=0
        print('Car was stoped')
    