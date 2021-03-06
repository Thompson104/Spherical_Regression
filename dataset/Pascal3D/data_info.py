from collections import OrderedDict as odict

__all__ = ['categories', 'category2nrmodel', 'VOC_classes', 'category2anchors', 'cadId2nrAnchors',  'cadId2anchornames' ]



category2nrmodel = odict([
      ('aeroplane'   ,  8),
      ('bicycle'     ,  6),
      ('boat'        ,  6),
      ('bottle'      ,  8),
      ('bus'         ,  6),
      ('car'         , 10),
      ('chair'       , 10),
      ('diningtable' ,  6),
      ('motorbike'   ,  5),
      ('sofa'        ,  6),
      ('train'       ,  4),
      ('tvmonitor'   ,  4),
])
#
categories = category2nrmodel.keys()


VOC_classes=['aeroplane'   ,
              'bicycle'    ,
              'bird'       ,
              'boat'       ,
              'bottle'     ,
              'bus'        ,
              'car'        ,
              'cat'        ,
              'chair'      ,
              'cow'        ,
              'diningtable',
              'dog'        ,
              'horse'      ,
              'motorbike'  ,
              'person'     ,
              'pottedplant',
              'sheep'      ,
              'sofa'       ,
              'train'      ,
              'tvmonitor'  ,]

# Warning: this might not correct, each cad model associate with a set anchors.
# They might be different even within same category.
category2anchors = odict([
    ('aeroplane' , ["left_elevator", "left_wing", "noselanding", "right_elevator",
                  "right_wing", "rudder_lower", "rudder_upper", "tail"]),
    ('bed'       , ["back_left", "back_right",
                  "frame_upper_left", "frame_upper_right",
                  "frame_lower_left", "frame_lower_right",
                  "mattres_upper_left", "mattres_upper_right",
                  "mattres_lower_left", "mattres_lower_right"]),
    ('boat'      , ["head", "head_down", "head_left", "head_right",
                  "tail_left", "tail_right", "tail"]),
    ('bicycle'   , ["head_center", "left_back_wheel", "left_front_wheel",
                  "left_handle", "left_pedal_center", "right_back_wheel",
                  "right_front_wheel", "right_handle", "right_pedal_center",
                  "seat_back", "seat_front"]),
    ('bottle'    , ["mouth", "body", "body_left", "body_right",
                  "bottom", "bottom_left", "bottom_right"]),
    ('bus'       , ["body_back_left_lower", "body_back_left_upper",
                  "body_back_right_lower", "body_back_right_upper",
                  "body_front_left_upper", "body_front_right_upper",
                  "body_front_left_lower", "body_front_right_lower",
                  "left_back_wheel", "left_front_wheel",
                  "right_back_wheel", "right_front_wheel"]),
    ('car'       , ["left_front_wheel", "left_back_wheel",
                  "right_front_wheel", "right_back_wheel",
                  "upper_left_windshield", "upper_right_windshield",
                  "upper_left_rearwindow", "upper_right_rearwindow",
                  "left_front_light", "right_front_light",
                  "left_back_trunk", "right_back_trunk"]),
    ('cellphone' , ["insidescreen_lower_left", "insidescreen_lower_right",
                  "insidescreen_upper_left", "insidescreen_upper_right",
                  "lowerkeyboard_lower_left", "lowerkeyboard_lower_right",
                  "lowerkeyboard_upper_left", "lowerkeyboard_upper_right",
                  "outsidescreen_lower_left", "outsidescreen_lower_right",
                  "outsidescreen_upper_left", "outsidescreen_upper_right",
                  "upperkeyboard_lower_left", "upperkeyboard_lower_right",
                  "upperkeyboard_upper_left", "upperkeyboard_upper_right"]),
    ('chair'     , ["back_upper_left", "back_upper_right",
                  "seat_upper_left", "seat_upper_right",
                  "seat_lower_left", "seat_lower_right",
                  "leg_upper_left", "leg_upper_right",
                  "leg_lower_left", "leg_lower_right"]),
    ('iron'      , ["handle_back", "handle_top", "back_left", "back_right", "tip"]),
    ('motorbike' , ["back_seat", "front_seat", "head_center", "headlight_center",
                  "left_back_wheel", "left_front_wheel","left_handle_center",
                  "right_back_wheel", "right_front_wheel", "right_handle_center"]),
    ('mouse'     , ["peak", "head", "scroll_lower", "scroll_upper", "tail"]),
    ('mug'       , ["bottom_near_handle", "bottom_opposite_handle",
                  "handle_bottom", "handle_top", "top_near_handle", "top_opposite_handle"]),
    ('shoe'      , ["back_bottom", "back_top", "front_bottom", "front_line", "front_top"]),
    ('sofa'      , ["front_bottom_left", "front_bottom_right",
                  "seat_bottom_left", "seat_bottom_right", "left_bottom_back",
                  "right_bottom_back", "top_left_corner",  "top_right_corner",
                  "seat_top_left", "seat_top_right"]),
    ('stapler'   , ["back_lower_left", "back_lower_right", "back_upper_left",
                  "back_upper_right", "front_upper_left",
                  "front_upper_right", "front_bottom_left", "front_bottom_right"]),
    ('diningtable' , ["leg_upper_left", "leg_upper_right", "leg_lower_left", "leg_lower_right",
                  "top_upper_left", "top_upper_right", "top_lower_left", "top_lower_right",
                  "top_up", "top_down", "top_left", "top_right"]),
    ('toaster'   , ["leftside_bottom_left", "leftside_bottom_right",
                  "leftside_top_left", "leftside_top_right",
                  "rightside_bottom_left", "rightside_bottom_right",
                  "rightside_top_left", "rightside_top_right"]),
    ('train'     , ["head_left_bottom", "head_left_top", "head_right_bottom", "head_right_top", "head_top",
                  "mid1_left_bottom", "mid1_left_top", "mid1_right_bottom", "mid1_right_top",
                  "mid2_left_bottom", "mid2_left_top", "mid2_right_bottom", "mid2_right_top",
                  "tail_left_bottom", "tail_left_top", "tail_right_bottom", "tail_right_top"]),
    ('tvmonitor' , ["front_bottom_left", "front_bottom_right",
                  "front_top_left", "front_top_right",
                  "back_bottom_left", "back_bottom_right",
                  "back_top_left", "back_top_right"]),
])


# cadId-to-Nr_anchors.
cadId2nrAnchors = odict([
    ('aeroplane01'       ,   8),
    ('aeroplane02'       ,   8),
    ('aeroplane03'       ,   8),
    ('aeroplane04'       ,   8),
    ('aeroplane05'       ,   8),
    ('aeroplane06'       ,   8),
    ('aeroplane07'       ,   8),
    ('aeroplane08'       ,   8),
    ('bus01'             ,  16),
    ('bus02'             ,  16),
    ('bus03'             ,  16),
    ('bus04'             ,  16),
    ('bus05'             ,  16),
    ('bus06'             ,  12),
    ('motorbike01'       ,  10),
    ('motorbike02'       ,  10),
    ('motorbike03'       ,  10),
    ('motorbike04'       ,  10),
    ('motorbike05'       ,  10),
    ('bicycle01'         ,  11),
    ('bicycle02'         ,  11),
    ('bicycle03'         ,  11),
    ('bicycle04'         ,  11),
    ('bicycle05'         ,  11),
    ('bicycle06'         ,  11),
    ('car01'             ,  20),
    ('car02'             ,  22),
    ('car03'             ,  12),
    ('car04'             ,  22),
    ('car05'             ,  20),
    ('car06'             ,  12),
    ('car07'             ,  20),
    ('car08'             ,  12),
    ('car09'             ,  20),
    ('car10'             ,  12),
    ('sofa01'            ,  10),
    ('sofa02'            ,  10),
    ('sofa03'            ,  10),
    ('sofa04'            ,  10),
    ('sofa05'            ,  10),
    ('sofa06'            ,  10),
    ('boat01'            ,   6),
    ('boat02'            ,   6),
    ('boat03'            ,   6),
    ('boat04'            ,   6),
    ('boat05'            ,   5),
    ('boat06'            ,   6),
    ('chair01'           ,  10),
    ('chair02'           ,  11),
    ('chair03'           ,  10),
    ('chair04'           ,  10),
    ('chair05'           ,  10),
    ('chair06'           ,  10),
    ('chair07'           ,  10),
    ('chair08'           ,  10),
    ('chair09'           ,  10),
    ('chair10'           ,   6),
    ('train01'           ,  16),
    ('train02'           ,   8),
    ('train03'           ,  11),
    ('train04'           ,   8),
    ('bottle01'          ,   9),
    ('bottle02'          ,   9),
    ('bottle03'          ,   9),
    ('bottle04'          ,   9),
    ('bottle05'          ,   9),
    ('bottle06'          ,   9),
    ('bottle07'          ,   9),
    ('bottle08'          ,   9),
    ('diningtable01'     ,   8),
    ('diningtable02'     ,   8),
    ('diningtable03'     ,   8),
    ('diningtable04'     ,   8),
    ('diningtable05'     ,   8),
    ('diningtable06'     ,   4),
    ('tvmonitor01'       ,   4),
    ('tvmonitor02'       ,   8),
    ('tvmonitor03'       ,   8),
    ('tvmonitor04'       ,   4),
])

#print max([x[1] for x in cadId2nrAnchors.items()])
#exit()


cadId2anchornames = odict([
    ('aeroplane01', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane02', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane03', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane04', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane05', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane06', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane07', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('aeroplane08', ['left_elevator', 'left_wing', 'noselanding', 'right_elevator', 'right_wing',
                        'rudder_lower', 'rudder_upper', 'tail']),
    ('bus01',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'left_headlight',
                        'leftcorner_windshield', 'right_back_wheel', 'right_front_wheel', 'right_headlight',
                        'rightcorner_windshield']),
    ('bus02',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'left_headlight',
                        'leftcorner_windshield', 'right_back_wheel', 'right_front_wheel', 'right_headlight',
                        'rightcorner_windshield']),
    ('bus03',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'left_headlight',
                        'leftcorner_windshield', 'right_back_wheel', 'right_front_wheel', 'right_headlight',
                        'rightcorner_windshield']),
    ('bus04',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'left_headlight',
                        'leftcorner_windshield', 'right_back_wheel', 'right_front_wheel', 'right_headlight',
                        'rightcorner_windshield']),
    ('bus05',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'left_headlight',
                        'leftcorner_windshield', 'right_back_wheel', 'right_front_wheel', 'right_headlight',
                        'rightcorner_windshield']),
    ('bus06',       ['body_back_left_lower', 'body_back_left_upper', 'body_back_right_lower',
                        'body_back_right_upper', 'body_front_left_lower', 'body_front_left_upper', 'body_front_right_lower',
                        'body_front_right_upper', 'left_back_wheel', 'left_front_wheel', 'right_back_wheel',
                        'right_front_wheel']),
    ('motorbike01', ['back_seat', 'front_seat', 'head_center', 'headlight_center', 'left_back_wheel',
                        'left_front_wheel', 'left_handle_center', 'right_back_wheel', 'right_front_wheel',
                        'right_handle_center']),
    ('motorbike02', ['back_seat', 'front_seat', 'head_center', 'headlight_center', 'left_back_wheel',
                        'left_front_wheel', 'left_handle_center', 'right_back_wheel', 'right_front_wheel',
                        'right_handle_center']),
    ('motorbike03', ['back_seat', 'front_seat', 'head_center', 'headlight_center', 'left_back_wheel',
                        'left_front_wheel', 'left_handle_center', 'right_back_wheel', 'right_front_wheel',
                        'right_handle_center']),
    ('motorbike04', ['back_seat', 'front_seat', 'head_center', 'headlight_center', 'left_back_wheel',
                        'left_front_wheel', 'left_handle_center', 'right_back_wheel', 'right_front_wheel',
                        'right_handle_center']),
    ('motorbike05', ['back_seat', 'front_seat', 'head_center', 'headlight_center', 'left_back_wheel',
                        'left_front_wheel', 'left_handle_center', 'right_back_wheel', 'right_front_wheel',
                        'right_handle_center']),
    ('bicycle01',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('bicycle02',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('bicycle03',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('bicycle04',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('bicycle05',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('bicycle06',   ['head_center', 'left_back_wheel', 'left_front_wheel', 'left_handle', 'left_pedal_center',
                        'right_back_wheel', 'right_front_wheel', 'right_handle', 'right_pedal_center', 'seat_back',
                        'seat_front']),
    ('car01',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'left_window_center', 'left_window_up', 'lower_left_rearwindow', 'lower_left_windshield',
                        'lower_right_rearwindow', 'lower_right_windshield', 'right_back_trunk', 'right_back_wheel',
                        'right_front_light', 'right_front_wheel', 'right_window_center', 'right_window_up',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car02',       ['left_back_light', 'left_back_trunk', 'left_back_wheel', 'left_front_light',
                        'left_front_wheel', 'left_window_center', 'left_window_up', 'lower_left_rearwindow',
                        'lower_left_windshield', 'lower_right_rearwindow', 'lower_right_windshield', 'right_back_light',
                        'right_back_trunk', 'right_back_wheel', 'right_front_light', 'right_front_wheel',
                        'right_window_center', 'right_window_up', 'upper_left_rearwindow', 'upper_left_windshield',
                        'upper_right_rearwindow', 'upper_right_windshield']),
    ('car03',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'right_back_trunk', 'right_back_wheel', 'right_front_light', 'right_front_wheel',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car04',       ['left_back_light', 'left_back_trunk', 'left_back_wheel', 'left_front_light',
                        'left_front_wheel', 'left_window_center', 'left_window_up', 'lower_left_rearwindow',
                        'lower_left_windshield', 'lower_right_rearwindow', 'lower_right_windshield', 'right_back_light',
                        'right_back_trunk', 'right_back_wheel', 'right_front_light', 'right_front_wheel',
                        'right_window_center', 'right_window_up', 'upper_left_rearwindow', 'upper_left_windshield',
                        'upper_right_rearwindow', 'upper_right_windshield']),
    ('car05',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'left_window_center', 'left_window_up', 'lower_left_rearwindow', 'lower_left_windshield',
                        'lower_right_rearwindow', 'lower_right_windshield', 'right_back_trunk', 'right_back_wheel',
                        'right_front_light', 'right_front_wheel', 'right_window_center', 'right_window_up',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car06',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'right_back_trunk', 'right_back_wheel', 'right_front_light', 'right_front_wheel',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car07',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'left_window_center', 'left_window_up', 'lower_left_rearwindow', 'lower_left_windshield',
                        'lower_right_rearwindow', 'lower_right_windshield', 'right_back_trunk', 'right_back_wheel',
                        'right_front_light', 'right_front_wheel', 'right_window_center', 'right_window_up',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car08',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'left_window_center', 'right_back_trunk', 'right_back_wheel', 'right_front_light',
                        'right_front_wheel', 'right_window_center', 'upper_left_rearwindow', 'upper_right_rearwindow']),
    ('car09',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'left_window_center', 'left_window_up', 'lower_left_rearwindow', 'lower_left_windshield',
                        'lower_right_rearwindow', 'lower_right_windshield', 'right_back_trunk', 'right_back_wheel',
                        'right_front_light', 'right_front_wheel', 'right_window_center', 'right_window_up',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('car10',       ['left_back_trunk', 'left_back_wheel', 'left_front_light', 'left_front_wheel',
                        'right_back_trunk', 'right_back_wheel', 'right_front_light', 'right_front_wheel',
                        'upper_left_rearwindow', 'upper_left_windshield', 'upper_right_rearwindow',
                        'upper_right_windshield']),
    ('sofa01',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('sofa02',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('sofa03',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('sofa04',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('sofa05',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('sofa06',      ['front_bottom_left', 'front_bottom_right', 'left_bottom_back', 'right_bottom_back',
                        'seat_bottom_left', 'seat_bottom_right', 'seat_top_left', 'seat_top_right', 'top_left_corner',
                        'top_right_corner']),
    ('boat01',      ['head', 'head_down', 'head_left', 'head_right', 'tail_left', 'tail_right']),
    ('boat02',      ['head', 'head_down', 'head_left', 'head_right', 'tail_left', 'tail_right']),
    ('boat03',      ['head', 'head_down', 'head_left', 'head_right', 'tail_left', 'tail_right']),
    ('boat04',      ['head', 'head_down', 'head_left', 'head_right', 'tail_left', 'tail_right']),
    ('boat05',      ['head', 'head_down', 'head_left', 'head_right', 'tail']), ('boat06', ['head', 'head_down',
                        'head_left', 'head_right', 'tail_left', 'tail_right']),
    ('chair01',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair02',     ['back_upper_left', 'back_upper_right', 'foot_center', 'left_handle_back',
                        'left_handle_front', 'right_handle_back', 'right_handle_front', 'seat_lower_left',
                        'seat_lower_right', 'seat_upper_left', 'seat_upper_right']),
    ('chair03',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair04',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair05',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair06',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair07',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair08',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair09',     ['back_upper_left', 'back_upper_right', 'leg_lower_left', 'leg_lower_right',
                        'leg_upper_left', 'leg_upper_right', 'seat_lower_left', 'seat_lower_right', 'seat_upper_left',
                        'seat_upper_right']),
    ('chair10',     ['back_upper_left', 'back_upper_right', 'seat_lower_left', 'seat_lower_right',
                        'seat_upper_left', 'seat_upper_right']),
    ('train01',     ['head_left_bottom', 'head_left_top', 'head_right_bottom', 'head_right_top',
                        'mid1_left_bottom', 'mid1_left_top', 'mid1_right_bottom', 'mid1_right_top', 'mid2_left_bottom',
                        'mid2_left_top', 'mid2_right_bottom', 'mid2_right_top', 'tail_left_bottom', 'tail_left_top',
                        'tail_right_bottom', 'tail_right_top']),
    ('train02',     ['head_left_bottom', 'head_left_top', 'head_right_bottom', 'head_right_top',
                        'mid1_left_bottom', 'mid1_left_top', 'mid1_right_bottom', 'mid1_right_top']),
    ('train03',     ['head_left_bottom', 'head_right_bottom', 'head_top', 'mid1_left_bottom', 'mid1_left_top',
                        'mid1_right_bottom', 'mid1_right_top', 'mid2_left_bottom', 'mid2_left_top', 'mid2_right_bottom',
                        'mid2_right_top']),
    ('train04',     ['head_left_bottom', 'head_left_top', 'head_right_bottom', 'head_right_top',
                        'mid1_left_bottom', 'mid1_left_top', 'mid1_right_bottom', 'mid1_right_top']),
    ('bottle01',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle02',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle03',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle04',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle05',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle06',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle07',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('bottle08',    ['body', 'body_left', 'body_right', 'bottom', 'bottom_left', 'bottom_right', 'mouth',
                        'mouth_left', 'mouth_right']),
    ('diningtable01',   ['leg_lower_left', 'leg_lower_right', 'leg_upper_left', 'leg_upper_right',
                        'top_lower_left', 'top_lower_right', 'top_upper_left', 'top_upper_right']),
    ('diningtable02',   ['leg_lower_left', 'leg_lower_right', 'leg_upper_left', 'leg_upper_right',
                        'top_lower_left', 'top_lower_right', 'top_upper_left', 'top_upper_right']),
    ('diningtable03',   ['leg_lower_left', 'leg_lower_right', 'leg_upper_left', 'leg_upper_right',
                        'top_lower_left', 'top_lower_right', 'top_upper_left', 'top_upper_right']),
    ('diningtable04',   ['leg_lower_left', 'leg_lower_right', 'leg_upper_left', 'leg_upper_right',
                        'top_lower_left', 'top_lower_right', 'top_upper_left', 'top_upper_right']),
    ('diningtable05',   ['leg_lower_left', 'leg_lower_right', 'leg_upper_left', 'leg_upper_right',
                        'top_lower_left', 'top_lower_right', 'top_upper_left', 'top_upper_right']),
    ('diningtable06',   ['top_down', 'top_left', 'top_right', 'top_up']),
    ('tvmonitor01',     ['front_bottom_left', 'front_bottom_right', 'front_top_left', 'front_top_right']),
    ('tvmonitor02',     ['back_bottom_left', 'back_bottom_right', 'back_top_left', 'back_top_right',
                        'front_bottom_left', 'front_bottom_right', 'front_top_left', 'front_top_right']),
    ('tvmonitor03',     ['back_bottom_left', 'back_bottom_right', 'back_top_left', 'back_top_right',
                                        'front_bottom_left', 'front_bottom_right', 'front_top_left', 'front_top_right']),
    ('tvmonitor04',     ['front_bottom_left', 'front_bottom_right', 'front_top_left', 'front_top_right'])
])
