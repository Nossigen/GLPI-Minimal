


	function set_new_object()
	{
		command_final_new = form_add_after('command_final', $('#new_object_data'));
		command_object_new = form_add_after('command_object', $('#new_object_data'));

		command_final_number = form_count('command_final');
		command_object_number = form_count('command_object');

		command_final_html = command_final_new.html().replace(/__TYPE__/g, $('#new_object_select :selected').text());
		command_object_html = command_object_new.html().replace(/__type__/g, $('#new_object_select :selected').text());

		command_object_new.find('.form_inner').remove();
		command_object_new.prepend(command_object_html);

		command_final_new.find('.form_inner').remove();
		command_final_new.prepend(command_final_html);

		command_final_new.attr('style', 'display: none;');

		// Set selection for objectType
		$('#id_form-' + (command_object_number - 1) + '-objectType').val(parsed_data[0].fields.objectType);

		return command_object_new;
	}

	function set_new_object_datas(data, command_object_new)
	{
		var i = 0;
		var new_object = '';

		while (data[i])
		{
			if (i == 0)
			{
				new_object = form_add_after('command_object_data', command_object_new);
			}
			else
			{
				new_object = form_add_after('command_object_data', new_object);
			}
		
			command_object_data_number = form_count('command_object_data');
			new_card = $('.' + select_last_form_name('command_object_data'));
	
			$('#id_form-' + (command_object_data_number - 1) + '-objectDataType').val(data[i].pk);
			new_html = new_card.html().replace(/__title__/g, data[i].fields.name);
			new_card.find('.form_inner').remove();
			new_card.prepend(new_html);
			i =  i + 1;
		}
		
		new_card.after("<div class='row'><a href='#' id='btn-form-end-" + (command_object_number - 1) + "' class='btn indigo right btn-validate-object'>Valider</a></div>");
		$('#btn-form-end-' + (command_object_number - 1)).click({'form_number': command_object_number - 1}, hide_object);
	}

	function hide_object(data)
	{
		// get values
		form_number = data.data.form_number;
		form_object = $('.form-' + form_number + '-command_object');
		form_object_type = $('#id_form-' + form_number + '-objectType').find('option:selected').text();
		form_object_name = $('.form-' + form_number + '-command_object').find('input').val();

		// Hide the input part
		$('.form-' + form_number + '-command_object').css('display', 'none');
		object_data = $('.form-' + form_number + '-command_object').next();

		var i = 0;
		while (object_data.next().attr('class') != 'row')
		{
			object_data.css('display', 'none');
			object_data = object_data.next();
		}
		object_data.next().css('display', 'none');
		object_data.css('display', 'none');

		console.log('-------test--------');
		set_final_form(object_data);
		console.log('-------test--------');
	}

	function set_final_form(object_data)
	{
		// object_data_final part
		to_fill = object_data.next().next();
		console.log('-------test--------');
		to_fill_new_html = to_fill.html().replace(/__NAME__/g, form_object_name);
		to_fill.find('.form_inner').remove();
		to_fill.append(to_fill_new_html);
		to_fill.css('display', '');
		object_number = $('.manage-object').find('#id_form-TOTAL_FORMS');
		console.log('------------test--------');
		console.log(object_number);
		nbr = parseInt(object_number.val());
		nbr = nbr + 1;
		object_number.val(nbr);
	}

	// New object //
	$('#new_object').click(
		function ()
		{
			$('#is').attr('style', '');
			$('#based_on').attr('style', 'display: none;');
		}
	);

$('#new_object_validate').click(
	function ()
	{
		var selected = parseInt($('#new_object_select').val());
		
		$.ajax(
				{
					url: '/object/new/get_type_form',
					data: {'objectType': selected},
					dataType: 'json',
					success: function (data)
					{
						parsed_data = eval(data.objectType);
						console.log('Ajax data get:');
						console.log(parsed_data);
						console.log('');
	
						command_object_new = set_new_object();
						command_object_number = form_count('command_object');

						set_new_object_datas(parsed_data, command_object_new);
					}
				}
		);
		$('#is').attr('style', 'display: none;');
	}
);
		

	// Existing object //
	$('#existing_object').click(
			function ()
			{
				$('#based_on').attr('style', '');
				$('#is').attr('style', 'display: none;');

			}
		);

	//////////////
	// VALIDATE //
	//////////////
