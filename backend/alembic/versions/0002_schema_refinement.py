"""schema_refinement

Revision ID: 0002_schema_refinement
Revises: 0001_initial_schema
Create Date: 2026-07-25 18:15:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '0002_schema_refinement'
down_revision: Union[str, None] = '0001_initial_schema'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename attacktypes to threattypes if exists, or create threattypes
    op.rename_table('attacktypes', 'threattypes')
    
    # Event model enhancements
    op.add_column('events', sa.Column('event_id', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('entity_id', sa.String(length=255), nullable=True))
    op.add_column('events', sa.Column('entity_type', sa.String(length=50), nullable=True))
    op.add_column('events', sa.Column('source_ip', sa.String(length=45), nullable=True))
    op.add_column('events', sa.Column('country', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('city', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('device_fingerprint', sa.String(length=255), nullable=True))
    op.add_column('events', sa.Column('browser', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('operating_system', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('authentication_method', sa.String(length=100), nullable=True))
    op.add_column('events', sa.Column('mfa_status', sa.String(length=50), nullable=True))
    op.add_column('events', sa.Column('vpn_status', sa.String(length=50), nullable=True))
    op.add_column('events', sa.Column('resource_accessed', sa.String(length=255), nullable=True))
    op.add_column('events', sa.Column('resource_sensitivity', sa.String(length=50), nullable=True))
    op.add_column('events', sa.Column('session_duration', sa.Float(), nullable=True))
    op.add_column('events', sa.Column('command_sequence', sa.Text(), nullable=True))
    op.add_column('events', sa.Column('raw_payload', sa.Text(), nullable=True))
    
    op.create_index(op.f('ix_events_entity_id'), 'events', ['entity_id'], unique=False)
    op.create_index(op.f('ix_events_event_id'), 'events', ['event_id'], unique=True)

    # BehaviourProfile model enhancements
    op.add_column('behaviourprofiles', sa.Column('typical_login_hours', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('typical_working_days', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('known_devices', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('known_countries', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('known_cities', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('known_resources', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('avg_session_duration', sa.Float(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('auth_preferences', sa.Text(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('behaviour_embedding_ref', sa.String(length=255), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('trust_score', sa.Float(), nullable=True))
    op.add_column('behaviourprofiles', sa.Column('risk_trend', sa.String(length=50), nullable=True))

    # UserSession model enhancements
    op.add_column('sessions', sa.Column('source_ip', sa.String(length=45), nullable=True))
    op.add_column('sessions', sa.Column('country', sa.String(length=100), nullable=True))
    op.add_column('sessions', sa.Column('city', sa.String(length=100), nullable=True))
    op.add_column('sessions', sa.Column('browser', sa.String(length=100), nullable=True))
    op.add_column('sessions', sa.Column('operating_system', sa.String(length=100), nullable=True))
    op.add_column('sessions', sa.Column('device_fingerprint', sa.String(length=255), nullable=True))
    op.add_column('sessions', sa.Column('vpn_status', sa.String(length=50), nullable=True))
    op.add_column('sessions', sa.Column('mfa_status', sa.String(length=50), nullable=True))
    op.add_column('sessions', sa.Column('auth_method', sa.String(length=100), nullable=True))
    op.add_column('sessions', sa.Column('session_risk', sa.Float(), nullable=True))
    op.add_column('sessions', sa.Column('start_time', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('sessions', sa.Column('end_time', sa.DateTime(timezone=True), nullable=True))

    # RiskScore model enhancements
    op.add_column('riskscores', sa.Column('behaviour_score', sa.Float(), nullable=True))
    op.add_column('riskscores', sa.Column('trust_score', sa.Float(), nullable=True))
    op.add_column('riskscores', sa.Column('context_score', sa.Float(), nullable=True))
    op.add_column('riskscores', sa.Column('threat_score', sa.Float(), nullable=True))
    op.add_column('riskscores', sa.Column('final_risk_score', sa.Float(), nullable=False, server_default='0.0'))
    op.add_column('riskscores', sa.Column('confidence', sa.Float(), nullable=True))
    op.add_column('riskscores', sa.Column('risk_level', sa.String(length=50), nullable=True))


def downgrade() -> None:
    op.rename_table('threattypes', 'attacktypes')
    # Revert additions if needed
    pass
