import logging
import json
import azure.functions as func


app = func.FunctionApp()


@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridTrigger_new(azeventgrid: func.EventGridEvent):


    logging.info('Function triggered to process a message: ', azeventgrid.get_body())
    logging.info('  EnqueuedTimeUtc =', azeventgrid.enqueued_time)
    logging.info('  SequenceNumber =', azeventgrid.sequence_number)
    logging.info('  Offset =', azeventgrid.offset)

    logging.info('Python EventGrid trigger processed an event')
    result = json.dumps({
        'id': azeventgrid.id,
        'data': azeventgrid.get_json(),
        'topic': azeventgrid.topic,
        'subject': azeventgrid.subject,
        'event_type': azeventgrid.event_type,
    })

    logging.info(f'Python EventGrid trigger processed an event: {result}')
