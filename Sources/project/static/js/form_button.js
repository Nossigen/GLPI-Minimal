function		set_form_checker(form_name)
{
	$(form_name + ' input').change({'form_name': form_name}, check_form);
	$(form_name + ' select').change({'form_name': form_name}, check_form);
}

function		check_form(data)
{

	form_name = data.data.form_name;

	var form_valid = true;

	$(form_name).find('input').each(
		function()
		{
			if($(this).prop('required'))
		    {
				if ($(this).val() == '')
					form_valid = false;
		    }
		}
		);
	$(form_name).find('select').each(
			function()
			{
				if($(this).prop('required'))
			    {
					if ($(this).val() == '')
						form_valid = false;
			    }
			}
		);
	if (form_valid == true)
	{
		$(form_name + ' .btn-submit').removeClass('disabled');
	}
	else
	{
		$(form_name + ' .btn-submit').addClass('disabled');		
	}
}