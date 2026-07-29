import re
from word2number import w2n

from livekit.agents import function_tool


class FoodTools:

    @function_tool
    async def get_order_status(self, order_id: str) -> str:

        print("\n========== TOOL ==========")
        print("Raw:", repr(order_id))

        order_id = order_id.lower().strip()

        # الحالة الأولى: يوجد أرقام بالفعل
        digits = re.findall(r"\d+", order_id)

        if digits:
            order_id = "".join(digits)

        else:
            # الحالة الثانية: الرقم مكتوب بالكلمات
            try:
                order_id = str(w2n.word_to_num(order_id))
            except Exception:
                # الحالة الثالثة:
                # five six five six five nine
                words = order_id.replace("-", " ").split()

                converted = []

                for word in words:
                    try:
                        converted.append(str(w2n.word_to_num(word)))
                    except Exception:
                        pass

                if converted:
                    order_id = "".join(converted)

        print("Normalized:", order_id)

        fake_db = {
            "1": "Order #1 is on the way and will arrive in about 15 minutes.",
            "25": "Order #25 has been delivered.",
            "565659": "Order #565659 is currently being prepared.",
        }

        result = fake_db.get(
            order_id,
            f"Order {order_id} was not found."
        )

        print("Result:", result)
        print("==========================\n")

        return result