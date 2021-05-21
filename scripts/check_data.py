from sdg.open_sdg import open_sdg_check

def alter_meta(meta, context):
    if context['data'] is not None and context['data'].empty == False:
        meta['reporting_status']='complete'
    return meta

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_meta=alter_meta)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
