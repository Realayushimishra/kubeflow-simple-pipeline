from kfp.compiler import Compiler
from kfp.components import load_component_from_file
from kfp.v2.dsl import pipeline

@pipeline(name='kube-poc')
def taxi_pipeline():
    fake = load_component_from_file('components/comp-1/component.yml')
    emote = load_component_from_file('components/comp-2/component.yml')

    fake_task = fake()
    emote_task = emote()    

Compiler().compile(taxi_pipeline, 'pipeline.yml')