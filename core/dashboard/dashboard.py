from django.utils import timezone
from django.db.models import Count
from tickets.models import Ticket
from django.db.models.functions import ExtractWeekDay


def meus_tickets(request):
	tickets = {
		'campo': Ticket.objects.filter(estado__campo=True, user_id=request.user.id,
                                       registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'pendencia': Ticket.objects.filter(estado__pendencia=True, user_id=request.user.id,
                                           registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'encerrado': Ticket.objects.filter(estado__encerrado=True, user_id=request.user.id,
                                           registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'total': Ticket.objects.filter(user_id=request.user.id,
                                       registrado_em__date=timezone.datetime.date(timezone.now())).count(),
	}
	return tickets


def tickets_equipe():
	tickets = {
		'campo': Ticket.objects.filter(estado__campo=True,
                                       registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'pendencia': Ticket.objects.filter(estado__pendencia=True,
                                           registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'encerrado': Ticket.objects.filter(estado__encerrado=True,
                                           registrado_em__date=timezone.datetime.date(timezone.now())).count(),
		'total': Ticket.objects.filter(registrado_em__date=timezone.datetime.date(timezone.now())).count(),
	}
	return tickets


def tickets_semana():
	inicio_semana = timezone.datetime.today().date() - timezone.timedelta(timezone.datetime.today().weekday())
	fim_semana = inicio_semana + timezone.timedelta(7)
	tickets = {
		'campo': Ticket.objects.filter(estado__campo=True,
                                       registrado_em__range=[inicio_semana, fim_semana]).count(),
		'pendencia': Ticket.objects.filter(estado__pendencia=True,
                                           registrado_em__range=[inicio_semana, fim_semana]).count(),
		'encerrado': Ticket.objects.filter(estado__encerrado=True,
                               			   registrado_em__range=[inicio_semana, fim_semana]).count(),
		'total': Ticket.objects.filter(registrado_em__range=[inicio_semana, fim_semana]).count(),
	}
	return tickets


def tickets_mes():
	tickets = {
		'campo': Ticket.objects.filter(estado__campo=True,
			                           registrado_em__year=timezone.datetime.today().year,
			                           registrado_em__month=timezone.datetime.today().month).count(),
		'pendencia': Ticket.objects.filter(estado__pendencia=True,
			                               registrado_em__year=timezone.datetime.today().year,
			                               registrado_em__month=timezone.datetime.today().month).count(),
		'encerrado': Ticket.objects.filter(estado__encerrado=True,
			                               registrado_em__year=timezone.datetime.today().year,
			                               registrado_em__month=timezone.datetime.today().month).count(),
		'total': Ticket.objects.filter(registrado_em__year=timezone.datetime.today().year,
                           			   registrado_em__month=timezone.datetime.today().month).count(),
	}
	return tickets


def tickets_sistema():
	return Ticket.objects.filter(registrado_em__year=timezone.datetime.today().year,
			                     registrado_em__month=timezone.datetime.today().month).values('empresa__sistema__nome').annotate(total=Count('empresa__sistema__nome'))


def tickets_top_5():
	return Ticket.objects.all().values('empresa__nome_fantasia').annotate(total=Count('empresa__nome_fantasia')).order_by('total')[:5]


def tickets_por_dia_semana():
	inicio_semana = timezone.datetime.today().date() - timezone.timedelta(timezone.datetime.today().weekday())
	fim_semana = inicio_semana + timezone.timedelta(7)
	return Ticket.objects.filter(registrado_em__range=[inicio_semana, fim_semana]).annotate(weekday=ExtractWeekDay('registrado_em')).values('weekday').annotate(count=Count('id')) .values('weekday', 'count')