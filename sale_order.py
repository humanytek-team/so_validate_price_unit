<<<<<<< HEAD
# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

	@api.multi
	def write(self, values):
		#print 'VALUES: ',values
		if 'order_line' in values:
			#print 'LEN_VALUES',len(values['order_line'])
			var = 0
			for line in values['order_line']:
				#print 'LINE: ', line[2]
				if line[2] != False and 'price_unit' in line[2]:
					#print 'PRECIO NUEVO: ', line[2]
					#print 'PRECIO ORIGINAL: ', self.order_line[var].price_unit
					if line[2]['price_unit'] < self.order_line[var].price_unit:
						#print 'PRECIO NUEVO ES MENOR AL PRECIO ORIGINAL'
						if self.is_member('Price Modify'):
							return super(sale_order,self).write(values)
						else:							
							raise ValidationError(_('Precio unitario muy bajo, favor de validarlo.\n-PRODUCTO (' + str(self.order_line[var].product_id.name) + ') PRECIO ORIGINAL (' + str(self.order_line[var].price_unit) + ')'))
							line[2]['price_unit'] = self.order_line[var].price_unit
					else:
						#print 'PRECIO NUEVO NO ES MENOR AL PRECIO ORIGINAL'
						return super(sale_order,self).write(values)
				var = var+1
			return super(sale_order,self).write(values)
		else:
			return super(sale_order,self).write(values)


	@api.multi 
	def is_member(self, group_name):
		'''METODO QUE DETERMINA SI EL USUARIO ES PARTE DE UN GRUPO
		LA VARIABLE GROUP_NAME CONTENDRA EL NOMBRE DEL GRUPO A BUSCAR'''
		##print 'IS_MEMBER'
		#print 'is_member'
		groups_obj = self.env['res.groups']
		group_id = groups_obj.search([('name','=',group_name)])[0]
		#rec = groups_obj.browse(group_id)
		rec = group_id
		##print 'REC: ',rec
		##print 'GRUPO: ',rec.name

		#SE RECORRE LA LISTA DE USUARIOS MIEMBROS DEL GRUPO Y SE VERIFICA SI EL UID SE ENCUENTRA EN ELLA
		if rec.users != None and rec.users != False:
			for user in rec.users:
				##print 'USAURIO: ',user.name
				if user.id == self._uid:
					#print 'ES TRUE'
					return True
		#print 'ES FALSO'
=======
# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

	@api.multi
	def write(self, values):
		#print 'VALUES: ',values
		if 'order_line' in values:
			#print 'LEN_VALUES',len(values['order_line'])
			var = 0
			for line in values['order_line']:
				#print 'LINE: ', line[2]
				if line[2] != False and 'price_unit' in line[2]:
					#print 'PRECIO NUEVO: ', line[2]
					#print 'PRECIO ORIGINAL: ', self.order_line[var].price_unit
					if line[2]['price_unit'] < self.order_line[var].price_unit:
						#print 'PRECIO NUEVO ES MENOR AL PRECIO ORIGINAL'
						if self.is_member('Price Modify'):
							return super(sale_order,self).write(values)
						else:							
							raise ValidationError(_('Precio unitario muy bajo, favor de validarlo.\n-PRODUCTO (' + str(self.order_line[var].product_id.name) + ') PRECIO ORIGINAL (' + str(self.order_line[var].price_unit) + ')'))
							line[2]['price_unit'] = self.order_line[var].price_unit
					else:
						#print 'PRECIO NUEVO NO ES MENOR AL PRECIO ORIGINAL'
						return super(sale_order,self).write(values)
				var = var+1
			return super(sale_order,self).write(values)
		else:
			return super(sale_order,self).write(values)


	@api.multi 
	def is_member(self, group_name):
		'''METODO QUE DETERMINA SI EL USUARIO ES PARTE DE UN GRUPO
		LA VARIABLE GROUP_NAME CONTENDRA EL NOMBRE DEL GRUPO A BUSCAR'''
		##print 'IS_MEMBER'
		#print 'is_member'
		groups_obj = self.env['res.groups']
		group_id = groups_obj.search([('name','=',group_name)])[0]
		#rec = groups_obj.browse(group_id)
		rec = group_id
		##print 'REC: ',rec
		##print 'GRUPO: ',rec.name

		#SE RECORRE LA LISTA DE USUARIOS MIEMBROS DEL GRUPO Y SE VERIFICA SI EL UID SE ENCUENTRA EN ELLA
		if rec.users != None and rec.users != False:
			for user in rec.users:
				##print 'USAURIO: ',user.name
				if user.id == self._uid:
					#print 'ES TRUE'
					return True
		#print 'ES FALSO'
>>>>>>> e64d0e302d01a7b4e9855253b8e5c6ba506232ed
		return False