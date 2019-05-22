			// A way to make dynamic formset with django

			// What you need before using it:
			// 
			// 	<div class="manage-[formset_name]">
			//		{{ [formset_name].management_form }}
			//	</div>
			//
			//	<div class="form-__prefix__-[formset_name]" style="display: none;">
			//		<div class='form_inner'>
			//			{{ [formset_name].empty_form }}
			//		</div>
			//	</div>

			// And you can use it like that:
			//
			//	form_add('[formset_name]');
			//
			//  or like that:
			//  
			// 	$('#button').click({'form_name': '[formset_name]'}, event_form_add);
						
			var				to_replace_base = '__prefix__';

			function		form_manage_update(form_name, form_count)
			{
				manager = $('.manage-' + form_name);

				manager.find('#id_form-TOTAL_FORMS').val(form_count);
			}

			function		form_count(form_name)
			{
				if ($('.' + 'form-' + 0 + '-' + form_name).length)
				{
					var i = 0;

					while ($('.' + 'form-' + i + '-' + form_name).length)
					{
						i = i + 1;
					}
					//console.log(form_name + ' trouvé: ' + i);
					return (i);
				}
				else
				{
					return 0;
				}
			}

			function		select_last_form_name(form_name)
			{
				var form_number = form_count(form_name);
				var last_form_div = '';

				if (form_number == 0)
				{
					last_form_div = 'form-' + '__prefix__' + '-' + form_name;
				}
				else
				{
					last_form_div = 'form-' + (form_number - 1)+ '-' + form_name;					
				}

				return last_form_div;
			}

			function		form_add(form_name)
			{
				base_form_div = $('.form-__prefix__-' + form_name);
				last_form_div = select_last_form_name(form_name);
				form_number = form_count(form_name);

				//console.log('form_add with: ' + form_name + ' form_name');
				//console.log('base_form_div: ' + base_form_div);
				//console.log('last_form_div: ' + last_form_div);
				//console.log('form_number: ' + form_number);

				// Select the template
				var new_form = $(base_form_div).clone(true);

				// Change __prefix__ to the form number
				new_html = new_form.html().replace(/__prefix__/g, form_number);
				new_form.find('.form_inner').remove();
				new_form.prepend(new_html);

				// Set new values
				new_form.attr('style', '');
				new_form.removeClass('form-__prefix__-' + form_name);
				new_form.addClass('form-' + form_number + '-' + form_name);
				new_form.insertAfter($('.' + last_form_div));

				form_manage_update(form_name, form_number + 1);
			}

			function		form_add_after(form_name, after)
			{
				base_form_div = $('.form-__prefix__-' + form_name);
				last_form_div = select_last_form_name(form_name);
				form_number = form_count(form_name);

				//console.log('form_add with: ' + form_name + ' form_name');
				//console.log('base_form_div: ' + base_form_div);
				//console.log('last_form_div: ' + last_form_div);
				//console.log('form_number: ' + form_number);

				// Select the template
				var new_form = $(base_form_div).clone(true);

				// Change __prefix__ to the form number
				new_html = new_form.html().replace(/__prefix__/g, form_number);
				new_form.find('.form_inner').remove();
				new_form.prepend(new_html);

				// Set new values
				new_form.attr('style', '');
				new_form.removeClass('form-__prefix__-' + form_name);
				new_form.addClass('form-' + form_number + '-' + form_name);
				to_return = new_form.insertAfter(after);

				form_manage_update(form_name, form_number + 1);
				return to_return;
			}

			function		event_form_add(data)
			{
				if (form_count(data.data.form_name) == 0)
				{
					form_add_after(data.data.form_name, $('.manage-' + data.data.form_name));
				}
				else
				{
					form_add(data.data.form_name);
				}
			}

			function		form_remove(form_name)
			{
				last_form_div = select_last_form_name(form_name);

				if (form_count(form_name) != 0)
				{
					$('.' + last_form_div).remove();
				}
			}

			function		event_form_remove(data)
			{
				form_remove(data.data.form_name);
			}
