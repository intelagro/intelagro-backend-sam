from db import Database


def catUnidadesProductivas(license: int):
    query = f'SELECT cat_holding_03_empresas_unidades_productivas.cat_holding_03_empresas_unidades_productivas_id, cat_holding_04_unidades_productivas_lotes.cat_holding_04_unidades_productivas_lotes_id, cat_holding_04_unidades_productivas_lotes.descripcion_lote AS lote, concat(cat_holding_03_empresas_unidades_productivas_categorias.descripcion_unidades_productivas_categorias, ": ", cat_holding_03_empresas_unidades_productivas.descripcion_unidades_productivas) AS descripcion FROM cat_holding_03_empresas_unidades_productivas LEFT OUTER JOIN cat_holding_03_empresas_unidades_productivas_categorias ON cat_holding_03_empresas_unidades_productivas.cat_holding_03_empresas_unidades_productivas_categorias_id = cat_holding_03_empresas_unidades_productivas_categorias.cat_holding_03_empresas_unidades_productivas_categorias_id LEFT OUTER JOIN cat_usuarios ON cat_holding_03_empresas_unidades_productivas.capturista = cat_usuarios.usuario LEFT OUTER JOIN cat_holding_04_unidades_productivas_lotes ON cat_holding_04_unidades_productivas_lotes.cat_holding_03_empresas_unidades_productivas_id = cat_holding_03_empresas_unidades_productivas.cat_holding_03_empresas_unidades_productivas_id WHERE (cat_usuarios_licencias_id = {license} AND cat_holding_03_empresas_unidades_productivas.vigente = 1);'
    data = Database.query(query)

    unidades_productivas = []
    up_list = []

    for element in data:
        if not element['cat_holding_03_empresas_unidades_productivas_id'] in up_list:
            unidades_productivas.append({
                'unidad_productiva_id': element['cat_holding_03_empresas_unidades_productivas_id'],
                'unidad_productiva_descripcion': element['descripcion'],
                'lotes': []
            })
            up_list.append(
                element['cat_holding_03_empresas_unidades_productivas_id'])

        for unidad_productiva in unidades_productivas:
            if unidad_productiva['unidad_productiva_id'] == element['cat_holding_03_empresas_unidades_productivas_id']:
                unidad_productiva['lotes'].append({
                    'lote_id': element['cat_holding_04_unidades_productivas_lotes_id'],
                    'lote_descripcion': element['lote']
                })
                break

    return unidades_productivas


def catPlagas(license: int):
    query = f'SELECT cat_control_plagas_y_enfermedades.cat_control_plagas_y_enfermedades_id AS plaga_id, concat(cat_control_plagas_y_enfermedades.descripcion_plaga_enfermedad, " - ", cat_control_plagas_y_enfermedades_categorias.descripcion_categoria_plaga_enfermedad) AS plaga_descripcion FROM cat_control_plagas_y_enfermedades INNER JOIN cat_usuarios ON cat_control_plagas_y_enfermedades.capturista = cat_usuarios.usuario LEFT OUTER JOIN cat_control_plagas_y_enfermedades_categorias ON cat_control_plagas_y_enfermedades.cat_control_plagas_y_enfermedades_categorias_id = cat_control_plagas_y_enfermedades_categorias.cat_control_plagas_y_enfermedades_categorias_id WHERE (cat_control_plagas_y_enfermedades.vigente =1 AND cat_usuarios_licencias_id = {license});'
    return Database.query(query)
