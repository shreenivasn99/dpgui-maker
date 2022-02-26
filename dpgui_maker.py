import dearpygui.dearpygui as dpg
from pandas import DataFrame

dpg.create_context()

command_list = ['add_2d_histogram_series',
 'add_3d_slider',
 'add_activated_handler',
 'add_active_handler',
 'add_alias',
 'add_area_series',
 'add_bar_series',
 'add_bool_value',
 'add_button',
 'add_candle_series',
 'add_char_remap',
 'add_checkbox',
 'add_child',
 'add_child_window',
 'add_clicked_handler',
 'add_clipper',
 'add_collapsing_header',
 'add_color_button',
 'add_color_edit',
 'add_color_picker',
 'add_color_value',
 'add_colormap',
 'add_colormap_button',
 'add_colormap_registry',
 'add_colormap_scale',
 'add_colormap_slider',
 'add_combo',
 'add_date_picker',
 'add_deactivated_after_edit_handler',
 'add_deactivated_handler',
 'add_double4_value',
 'add_double_value',
 'add_drag_float',
 'add_drag_floatx',
 'add_drag_int',
 'add_drag_intx',
 'add_drag_line',
 'add_drag_payload',
 'add_drag_point',
 'add_draw_layer',
 'add_draw_node',
 'add_drawlist',
 'add_dummy',
 'add_dynamic_texture',
 'add_edited_handler',
 'add_error_series',
 'add_file_dialog',
 'add_file_extension',
 'add_filter_set',
 'add_float4_value',
 'add_float_value',
 'add_float_vect_value',
 'add_focus_handler',
 'add_font',
 'add_font_chars',
 'add_font_range',
 'add_font_range_hint',
 'add_font_registry',
 'add_group',
 'add_handler_registry',
 'add_heat_series',
 'add_histogram_series',
 'add_hline_series',
 'add_hover_handler',
 'add_image',
 'add_image_button',
 'add_image_series',
 'add_input_float',
 'add_input_floatx',
 'add_input_int',
 'add_input_intx',
 'add_input_text',
 'add_int4_value',
 'add_int_value',
 'add_item_activated_handler',
 'add_item_active_handler',
 'add_item_clicked_handler',
 'add_item_deactivated_after_edit_handler',
 'add_item_deactivated_handler',
 'add_item_edited_handler',
 'add_item_focus_handler',
 'add_item_handler_registry',
 'add_item_hover_handler',
 'add_item_resize_handler',
 'add_item_toggled_open_handler',
 'add_item_visible_handler',
 'add_key_down_handler',
 'add_key_press_handler',
 'add_key_release_handler',
 'add_knob_float',
 'add_line_series',
 'add_listbox',
 'add_loading_indicator',
 'add_menu',
 'add_menu_bar',
 'add_menu_item',
 'add_mouse_click_handler',
 'add_mouse_double_click_handler',
 'add_mouse_down_handler',
 'add_mouse_drag_handler',
 'add_mouse_move_handler',
 'add_mouse_release_handler',
 'add_mouse_wheel_handler',
 'add_node',
 'add_node_attribute',
 'add_node_editor',
 'add_node_link',
 'add_pie_series',
 'add_plot',
 'add_plot_annotation',
 'add_plot_axis',
 'add_plot_legend',
 'add_progress_bar',
 'add_radio_button',
 'add_raw_texture',
 'add_resize_handler',
 'add_same_line',
 'add_scatter_series',
 'add_selectable',
 'add_separator',
 'add_series_value',
 'add_shade_series',
 'add_simple_plot',
 'add_slider_float',
 'add_slider_floatx',
 'add_slider_int',
 'add_slider_intx',
 'add_spacer',
 'add_spacing',
 'add_stage',
 'add_staging_container',
 'add_stair_series',
 'add_static_texture',
 'add_stem_series',
 'add_string_value',
 'add_subplots',
 'add_tab',
 'add_tab_bar',
 'add_tab_button',
 'add_table',
 'add_table_cell',
 'add_table_column',
 'add_table_next_column',
 'add_table_row',
 'add_template_registry',
 'add_text',
 'add_text_point',
 'add_texture_registry',
 'add_theme',
 'add_theme_color',
 'add_theme_component',
 'add_theme_style',
 'add_time_picker',
 'add_toggled_open_handler',
 'add_tooltip',
 'add_tree_node',
 'add_value_registry',
 'add_viewport_drawlist',
 'add_viewport_menu_bar',
 'add_visible_handler',
 'add_vline_series',
 'add_window']


config = DataFrame(columns=['tags','methods','name','parent','params','container or not'])
config.set_index('tags',inplace=True)
containers = ['Primary Window']

with dpg.window(tag='This Primary Window'):
    dpg.add_group(tag='main',horizontal=True)
    # Left Navigation
    with dpg.child_window(width=300,parent='main',tag='left'):
        dpg.add_text(default_value='Add item methods')
        dpg.add_listbox(items=command_list,num_items=len(command_list),width=300,tag='lb')
    # Centre Display    
    with dpg.child_window(width=900,parent='main',tag='centre'):
        def item_selected(sender,app_data,user_data):
            tag= user_data
            print(config['name'][tag])
            dpg.set_value(item='item_tag',value=tag)
            dpg.set_value(item='item_name',value=config['name'][tag])
            dpg.set_value(item='item_parent',value=config['parent'][tag])
            dpg.set_value(item='other_param',value=config['params'][tag])
            
        dpg.add_text(default_value='Structure of items')
        dpg.add_window(tag='Primary Window',pos=(400,50),collapsed=True)
        dpg.add_tree_node(label='Primary Window',tag='coll_Primary Window')
        
    # Right Display
    with dpg.child_window(width=400,parent='main',tag='right'):
        # Items control area
        with dpg.child_window(height=200,width=400,parent='right'):
            dpg.add_input_text(tag='item_name',label='Name',width=200)
            dpg.add_input_text(tag='item_tag',label='Tag',width=200)
            dpg.add_listbox(items=containers,tag='item_parent',label='Parent')
            dpg.add_input_text(tag='other_param',label='Other parameters',width=200)
        # Buttons callback
        def add_or_modify_item(sender,app_data,user_data):
            tag = dpg.get_value('item_tag')
            name = dpg.get_value('item_name')
            parent = dpg.get_value('item_parent')
            params = dpg.get_value('other_param')
                    
            method = 'dpg.' + dpg.get_value('lb') + '(tag="{0}",label="{1}",parent="{2}",{3})'.format(tag,name,parent,params)
            print(method)  
            
            if user_data=='add':
                if tag != '' and tag not in config.index:                    
                    exec(method)
                    cont_bool = dpg.is_item_container(tag)
                    if cont_bool:
                        dpg.add_tree_node(label=name,parent='coll_'+ parent, tag= 'coll_' + tag,drop_callback=item_selected)
                        containers.append(tag)
                        dpg.configure_item(item='item_parent',items=containers)
                    else:
                        dpg.add_radio_button(items=[name],tag='coll_' + tag, parent='coll_'+ parent,callback=item_selected,user_data=tag)
                    config.loc[tag]= [method,name,parent,params,cont_bool]
                    
            elif user_data=='modify':
                cont_bool = config['container or not'][tag]
                dpg.configure_item(item=tag,label=name,parent=parent)
                
                print('item=tag,'+dpg.get_value('other_param'))
                exec('dpg.configure_item(item=tag,'+dpg.get_value('other_param')+')')               
                
                if cont_bool:
                    dpg.configure_item(item='coll_' + tag, label=name)
                else:
                    dpg.configure_item(item='coll_' + tag, items=[name])
                
                config.loc[tag]= [method,name,parent,params,cont_bool]

                
            dpg.set_value('other_param','') # To avoid previous parameters affecting creation of new item  

        def remove_item():
            tag = dpg.get_value('item_tag')
            dpg.delete_item(item=tag)
            dpg.delete_item(item='coll_'+tag)
            config.drop(tag,inplace=True)
            
        # Buttons
        with dpg.group(horizontal=True,parent='right'):
            dpg.add_button(label='Add item',callback=add_or_modify_item,user_data='add')
            dpg.add_button(label='Modify item',callback=add_or_modify_item,user_data='modify')
            dpg.add_button(label='Delete item',callback=remove_item)
        
        def save():
            with open('your_project.py','w') as file:
                for line in config['methods']:
                    file.writelines("{}\n".format(line))
                    
        dpg.add_button(label="Save",callback=save)   
  
dpg.create_viewport(title='Custom Title', width=1600, height=900,x_pos=0,y_pos=0)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("This Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


