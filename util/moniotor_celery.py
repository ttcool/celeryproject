from celery import Celery
def my_monitor(app):
    state = app.events.State()

    def announce_failed_tasks(event):
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s %s [%s] %s' % (task.name, task.hostname, task.uuid, task.timestamp, task.info(),))

    def announce_receive_tasks(event):
        state.event(event)
        # task name is sent only with -received event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK RECEIVED: %s %s [%s] %s' % (task.name, task.hostname, task.uuid, task.timestamp, task.info(),))

    def announce_succeeded_tasks(event):
        state.event(event)
        # task name is sent only with -succeeded event, and state
        # will keep track of this for us.
        task = state.tasks.get(event['uuid'])

        print('TASK SUCCEEDED: %s %s [%s] %s' % (task.name, task.hostname, task.uuid, task.timestamp, task.info(),))

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-failed': announce_failed_tasks,
                #'task-received': announce_receive_tasks,
                'task-succeeded': announce_succeeded_tasks,
                '*': state.event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    print('monitor start')
    app = Celery(broker='redis://192.168.1.10:6379/2')
    my_monitor(app)
