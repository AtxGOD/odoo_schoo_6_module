from odoo import models


class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'

    def all_books_list(self):
        """Extends the Categories model
           The method returns a list of all books by the selected category

           :return object:
           """

        # get list view
        view_id_list = self.env.ref('school_lesson_6_1.library_book_view_tree').id
        return {
            'type': 'ir.actions.act_window',
            'name': 'Show all books',
            'res_model': 'library.book',
            'domain': [('category_id', '=', self.id)],
            'context': {},
            'views': [[view_id_list, 'tree'], [False, 'form']],
            'target': 'current',
        }
