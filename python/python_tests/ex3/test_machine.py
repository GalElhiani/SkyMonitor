#Author: Gal Elhiani
#Tester: Tomer Bahar

import pytest
from datetime import datetime
# Assuming your production code is in a file named machine_service.py
from machine import Machine, MachineType1, MachineType2

class TestMachine:

    @pytest.fixture
    def type1_machine(self):
        return MachineType1(type=1, name="a")

    @pytest.fixture
    def type2_machine(self):
        return MachineType2(type=2, name="b")


    def test_initial_state(self, type1_machine):
        assert type1_machine.type == 1
        assert type1_machine.name == "a"
        assert type1_machine.cpm == 2
        assert type1_machine.is_running is False
        assert type1_machine.start_time is None
        assert type1_machine.stop_time is None

    def test_start_machine(self, type1_machine):
        test_time = datetime(2026, 7, 5, 12, 0, 0)
        
        type1_machine.start_machine(current_time=test_time)
        
        assert type1_machine.is_running is True
        assert type1_machine.start_time == test_time

    def test_stop_machine(self, type1_machine):
        type1_machine.is_running = True
        type1_machine.start_time = datetime(2026, 7, 5, 12, 0, 0)
        test_time = datetime(2026, 7, 5, 12, 30, 0)

        type1_machine.stop_machine(current_time=test_time)

        assert type1_machine.is_running is False
        assert type1_machine.stop_time == test_time

    def test_stop_already_off_raises_error(self, type1_machine):
        # Default state is off, so calling stop should throw an error
        with pytest.raises(RuntimeError) as exc_info:
            type1_machine.stop_machine()
        
        assert str(exc_info.value) == "the machine is already off!"


    def test_get_time_never_started(self, type1_machine):
        assert type1_machine.get_time() == 0

    def test_get_price_while_running(self, type1_machine):
        type1_machine.is_running = True
        type1_machine.start_time = datetime(2026, 7, 5, 12, 0, 0)
        check_time = datetime(2026, 7, 5, 12, 30, 0)

        assert type1_machine.get_price(current_time=check_time) == 60.0

    def test_get_price_after_stopped(self, type2_machine):
        type2_machine.is_running = False
        type2_machine.start_time = datetime(2026, 7, 5, 12, 0, 0)
        type2_machine.stop_time = datetime(2026, 7, 5, 12, 10, 0)

        assert type2_machine.get_price() == 50.0


    def test_get_total_price(self):
        Machine.tracking_table = []

        m1 = MachineType1(1, "t1-instance")
        m1.is_running = True
        m1.start_time = datetime(2026, 7, 5, 12, 0, 0)

        m2 = MachineType2(2, "t2-instance")
        m2.is_running = True
        m2.start_time = datetime(2026, 7, 5, 12, 0, 0)

        check_time = datetime(2026, 7, 5, 12, 10, 0)

        total_billing = Machine.get_total_price(current_time=check_time)

        assert total_billing == 70.0        #20 + 50 = 70
